import cv2 as cv

#thay đổi img từ 01.jpeg -> 05.jpeg
img = cv.imread("05.jpeg", 0)   #chỉ đọc đc jpeg
dim = (1100, 650)
dimg = cv.resize(img, dim, interpolation = cv.INTER_AREA)

#01.jpeg
#kernel1 = cv.getStructuringElement(cv.MORPH_RECT, (1,4))    #kernel 01.jpeg
#ret, thresh = cv.threshold(dimg, 130, 160, cv.THRESH_BINARY)
#di = cv.erode(thresh, kernel1, iterations = 1)
#cv.imshow("@1", dimg)
#cv.imshow("01", di)
#cv.imwrite("out1.jpeg", di)

#04.jpeg
#kernel4 = cv.getStructuringElement(cv.MORPH_RECT, (2,2))     #kernel 04.jpeg
#ret, thresh = cv.threshold(dimg, 100, 150, cv.THRESH_BINARY)
#dimgx = cv.dilate(thresh, kernel4, iterations = 1)
#cv.imshow("@4", dimg)
#cv.imshow("04", dimgx)
#cv.imwrite("out4.jpeg", dimgx)

#05.jpeg
cv.imshow("@5", dimg)
kernel5 = cv.getStructuringElement(cv.MORPH_RECT, (2,1))    #kernel: làm thon ảnh
di = cv.dilate(dimg, kernel5, iterations = 1)
ret, thresh = cv.threshold(di, 175, 190, cv.THRESH_BINARY)
kernel55 = cv.getStructuringElement(cv.MORPH_RECT, (2,5))   #kernel: xử lý theo chiều doc (do barcode chiều dọc)
er = cv.erode(thresh, kernel55, iterations = 1)
cv.imshow("@5", dimg)
cv.imshow("05", er)
cv.imwrite("out5.jpeg", er)

#03.jpeg
#cv.imshow("@3", dimg)
#kernel3 = cv.getStructuringElement(cv.MORPH_RECT, (3,1))   #Barcode nằm theo chiều ngang
#di = cv.dilate(dimg, kernel3, iterations = 1)
#ret, thresh = cv.threshold(di, 175, 195, cv.THRESH_BINARY)
#cv.imshow("03", thresh)
#cv.imwrite("out3.jpeg", thresh)

#02.jpeg (not done yet)
#cv.imshow("@2", dimg)
#kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (1,5))
#di = cv.dilate(dimg, kernel2, iterations = 1)
#cv.imshow("22", di)
#ret, thresh = cv.threshold(di, 50, 255, cv.THRESH_BINARY)
#cv.imshow("2", thresh)


cv.waitKey(0)
cv.destroyAllWindows()