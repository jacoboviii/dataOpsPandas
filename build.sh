pyinstaller app.py \
    --clean \
    --hidden-import "clr" --name "DataOps" \
    --icon "icon.icns" \
    --paths "/Users/jacoboperez/anaconda3/envs/" \
    --add-data "templates:./templates/" \
    --add-data "dataProcess.py:./" \