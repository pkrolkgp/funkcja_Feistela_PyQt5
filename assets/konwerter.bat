magick "%~1" -resize 256x256 -gravity center -background none -extent 256x256 -define icon:auto-resize="256,128,96,64,48,32,16" "%~n1.ico"
pause