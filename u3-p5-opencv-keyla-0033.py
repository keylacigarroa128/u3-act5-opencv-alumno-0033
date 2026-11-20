##  Procesamiento de imágenes con OpenCV
## Keyla paola NC = 0033 | Fecha 20/nov/2026
import cv2 
print(" --- Lectura y visualización de imágenes Keyla Paola NC = 0033---")
# Leer la imagen del archivo
image = cv2.imread( 'leonkennedy.jpg' ) 
# Mostrar la imagen en una ventana
cv2.imshow( 'leon kennedy Keyla Paola NC = 0033' , image) 
# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0) 
cv2.destroyAllWindows()

print("--- Conversión entre espacios de color Keyla Paola NC = 0033 ---")
# Cargar la imagen
image = cv2.imread( 'leonkennedy.jpg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Guardar la imagen en escala de grises
cv2.imwrite(  'gray_image.jpg' , gray_image)

print("---Cambiar el tamaño de una imagen---")
# Cargar la imagen
image = cv2.imread( 'leonkennedy.jpg' ) 
# Redimensionar la imagen a 300x200
resized_image = cv2.resize(image, (300, 200)) 
# Guardar la imagen redimensionada
cv2.imwrite( 'resized_image.jpg' , resized_image)

print("--- Rotar una imagen --- ")
# Cargar la imagen
image = cv2.imread('leonkennedy.jpg') 
# Obtener la altura y el ancho de la imagen
(h, w) = image.shape[:2] 
# Definir el centro de la imagen
center = (w // 2, h // 2) 
matrix = cv2.getRotationMatrix2D(center, 90, 1.0) 
# Realizar la rotación
rotated_image = cv2.warpAffine(image, matrix, (w, h)) 
# Guardar la imagen rotada
cv2.imwrite('rotated_image_leon_kennedy 0033.jpg', rotated_image)

print("-- Desenfoque de una imagen --")
# Cargar la imagen
image = cv2.imread( 'leonkennedy.jpg' ) 
# Aplicar desenfoque gaussiano
blured_image = cv2.GaussianBlur(image, (15, 15), 0) 
# Guardar la imagen desenfocada
cv2.imwrite( 'blurred_image_leon_kennedy_0033.jpg' , blured_image)

print("Detección de bordes mediante el algoritmo de Canny")
# Cargar la imagen
image = cv2.imread( 'leonkennedy.jpg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100 , 200 ) 
# Guardar la imagen de bordes
cv2.imwrite( 'edges Keyla Paola NC = 0033.jpg' , edges)

print("Dibujar formas y añadir texto")
# Cargar la imagen
image = cv2.imread( 'leonkennedy.jpg' ) 
# Dibujar un rectángulo
cv2.rectangle(image, ( 50 , 50 ), ( 200 , 200 ), ( 255 , 0 , 0 ), 3 ) 
# Agregar texto a la imagen
cv2.putText(image, 'OpenCV' , ( 60 , 40 ), cv2.FONT_HERSHEY_SIMPLEX, 1 , ( 0 , 255 , 0 ), 2 ) 
# Guardar la imagen de salida
cv2.imwrite( 'output_image Keyla Paola NC = 0033.jpg' , image)

print("Umbralización")
# Cargar la imagen
image = cv2.imread( 'leonkennedy.jpg' , 0 ) 
# Aplicar umbralización
_, thresh_image = cv2.threshold(image, 127 , 255 , cv2.THRESH_BINARY) 
# Guardar la imagen umbralizada
cv2.imwrite( 'threshold_image Keyla Paola NC = 0033.jpg' , thresh_image )

print("Detección de contornos")
# Cargar la imagen
image = cv2.imread('leonkennedy.jpg')

# Verificar que la imagen se haya cargado
if image is None:
    print("Error: No se encontró la imagen.")
else:
    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Encontrar bordes
    edges = cv2.Canny(gray_image, 100, 200)
    # Encontrar contornos
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    # Dibujar contornos en la imagen original
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    # Guardar la imagen de salida con contornos
    cv2.imwrite('contours_image Keyla Paola NC = 0033.jpg', image)
    # Mostrar el resultado
    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()