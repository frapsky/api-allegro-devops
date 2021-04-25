import os
import sys
import shutil
from PIL import Image
import asyncio
from aiofile import AIOFile, Reader, Writer
from fastapi import FastAPI, File, UploadFile,Response, status
from fastapi.responses import FileResponse,JSONResponse
from hypercorn.config import Config
from hypercorn.asyncio import serve
import uvicorn


app = FastAPI()

@app.post("/api/rotate")
async def image(image: UploadFile = File(...)):

    file_location = f"{image.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(image.file, file_object)   
    
    img = Image.open(image.filename)
    photo = img.convert('RGB')
    #print("Size before convert", img.size)
    #print("Size after convert", photo.size)
    
    width = photo.size[0] 
    height = photo.size[1]
    
    czyPrzeiterowalesObrazekHorizontal = False
    czyPrzeiterowalesObrazekVertical = False

    horizontalWhiteRedLineExists = False
    horizontalRedWhiteLineExists = False
    verticalWhiteRedLineExists = False
    verticalRedWhiteLineExists = False

    existingHorizontalLinesCount=0
    existingVerticalLinesCount=0

    countX=0
    countY=0

    listOfPixels = []

    for y in range(height): #horizontal line
        
        for x in range(width):

            RGB = photo.getpixel((x,y)) ## [wh][wh][wh][r][r][r]
            #[R, G, B]
            R,G,B = RGB 
            if RGB == (255,255,255) and photo.getpixel(((x-1),y)) != (255, 255, 255): 
                for row in range(0,6):
                    listOfPixels.append(photo.getpixel(((x+row),y))) 
                    #print(listOfPixels)
                    if len(listOfPixels)==6:
                        #
                        #print(listOfPixels)
                        if listOfPixels[0] == (255,255,255) and listOfPixels[1] == (255,255,255) and listOfPixels[2] == (255,255,255) and listOfPixels[3] == (255,0,0) and listOfPixels[4] == (255,0,0) and listOfPixels[5] == (255,0,0):
                            horizontalWhiteRedLineExists = True
                            #print(listOfPixels)
                            existingHorizontalLinesCount+=1  
                            listOfPixels.clear()
                        else: 
                            listOfPixels.clear() 


            if RGB == (255,0,0) and photo.getpixel(((x-1),y)) != (255, 255, 255) and photo.getpixel(((x-1),y)) != (255, 0, 0): 
                for row in range(0,6):
                    listOfPixels.append(photo.getpixel(((x+row),y))) 
                    #print(listOfPixels)
                    if len(listOfPixels)==6:
                        #
                        #print(listOfPixels)
                        if listOfPixels[0] == (255,0,0) and listOfPixels[1] == (255,0,0) and listOfPixels[2] == (255,0,0) and listOfPixels[3] == (255,255,255) and listOfPixels[4] == (255,255,255) and listOfPixels[5] == (255,255,255):
                            horizontalRedWhiteLineExists = True
                            #print(listOfPixels)
                            existingHorizontalLinesCount+=1  
                            listOfPixels.clear()
                        else: 
                            listOfPixels.clear()                       
            countX+=1
        countY+=1
        if countY==height and (countX/countY) == width:
            czyPrzeiterowalesObrazekHorizontal=True
            #print("Liczba x",(int)(countX/countY), "Liczba y: ", countY)
            countX=0
            countY=0


    for x in range(width): #vertical line
        
        for y in range(height):

            RGB = photo.getpixel((x,y)) ## [wh][wh][wh][r][r][r]
            #[R, G, B]
            R,G,B = RGB 
            if RGB == (255,255,255) and photo.getpixel((x,y-1)) != (255, 255, 255): 
                for column in range(0,6):
                    listOfPixels.append(photo.getpixel((x,y+column))) 
                    #print(listOfPixels)
                    if len(listOfPixels)==6:
                        #
                        #print(listOfPixels)
                        if listOfPixels[0] == (255,255,255) and listOfPixels[1] == (255,255,255) and listOfPixels[2] == (255,255,255) and listOfPixels[3] == (255,0,0) and listOfPixels[4] == (255,0,0) and listOfPixels[5] == (255,0,0):
                            verticalWhiteRedLineExists = True
                            #print(listOfPixels)
                            existingVerticalLinesCount+=1  
                            listOfPixels.clear()
                        else: 
                            listOfPixels.clear() 


            if RGB == (255,0,0) and photo.getpixel(((x-1),y)) != (255, 255, 255) and photo.getpixel(((x-1),y)) != (255, 0, 0): 
                for column in range(0,6):
                    listOfPixels.append(photo.getpixel((x,y+column))) 
                    #print(listOfPixels)
                    if len(listOfPixels)==6:
                        #print(listOfPixels)
                        if listOfPixels[0] == (255,0,0) and listOfPixels[1] == (255,0,0) and listOfPixels[2] == (255,0,0) and listOfPixels[3] == (255,255,255) and listOfPixels[4] == (255,255,255) and listOfPixels[5] == (255,255,255):
                            verticalRedWhiteLineExists = True
                            #print(listOfPixels)
                            existingVerticalLinesCount+=1  
                            listOfPixels.clear()
                        else: 
                            listOfPixels.clear()                       
            countX+=1
        countY+=1
        if countY==height and (countX/countY) == width:
            czyPrzeiterowalesObrazekHorizontal=True
            #print("Liczba x",(int)(countX/countY), "Liczba y: ", countY)

    
    # print("Ilosc linii poziomych: ",existingHorizontalLinesCount)
    # print("Ilosc linii pionowych: ",existingVerticalLinesCount)
    # print("Czy pozioma biala linia istnieje: ",horizontalWhiteRedLineExists)    
    # print("Czy pozioma czerwona linia istnieje: ",horizontalRedWhiteLineExists) 
    # print("Czy pionowa biala linia istnieje: ",verticalWhiteRedLineExists)    
    # print("Czy pionowa czerwona linia istnieje: ",verticalRedWhiteLineExists) 
    # print("Czy przeiterowales po kazdym pixelu: ", czyPrzeiterowalesObrazekHorizontal)

    
    #  Po wykryciu takiej linii, aplikacja powinna obrócić obraz w taki sposób, aby linia umieszczona była pionowo, białymi pikselami
    #  do góry.
    
    if horizontalWhiteRedLineExists:
        rotate_img = photo.transpose(Image.ROTATE_270)
        rotate_img.save("rotatedImage.png")
        return FileResponse("rotatedImage.png",status_code=status.HTTP_200_OK)

    #  W przypadku, jeśli obraz źródłowy zawiera linię pionową z białymi pikselami na dole, należy wykonać obrót zdjęcia o
    #  180 stopni, a nie odbicie lustrzane.

    if verticalRedWhiteLineExists:
        rotate_img = photo.transpose(Image.ROTATE_180)
        rotate_img.save("rotatedImage.png")
        return FileResponse("rotatedImage.png",status_code=status.HTTP_200_OK)

    if verticalRedWhiteLineExists == False and verticalWhiteRedLineExists == False and horizontalRedWhiteLineExists == False and horizontalWhiteRedLineExists== False:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST)



if __name__ == '__main__':
        uvicorn.run(app, port=8000, host="0.0.0.0")

