from flask import Flask, render_template, request
def location():
    # TODO: 從資料庫讀檔
    # 燃油車維修地點
    fuelCar = ["高雄市三民區建工路415號", "高雄市燕巢區深中路58號"]
    # GOGORO 維修地點
    gogoroRepair = ["高雄市三民區建工路415號", "高雄市燕巢區深中路58號"]
    # GOGORO 換電地點
    gogoroReplacement = ["高雄市三民區建工路415號", "高雄市燕巢區深中路58號"]
    return render_template("location/location.html", fuelCar=fuelCar,
            gogoroRepair=gogoroRepair, gogoroReplacement=gogoroReplacement)

