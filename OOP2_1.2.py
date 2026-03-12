# Tinh tong so giay tu 42 phut va 42 giay
seconds=(42*60+42)
print(f"Tong so giay: {seconds} giay")

# Doi tu kilomet sang dam
kilometers = 10
miles = kilometers / 1.61
print(f"tong so dam trong 10 km: {miles:.2f} dam ")

# Tinh thoi gian trung binh
pace_in_seconds =seconds/miles
pace_minutes=int(pace_in_seconds//60)
pace_in_seconds=int(pace_in_seconds%60)
print(f"pace trung binh tren mot dam: {pace_minutes} phut {pace_in_seconds} giay moi dam ")

# van toc trung binh dam/gio
hours= seconds/3600
speed= miles/hours
print(f"van toc trong binh; {speed:2f} dam/gio")
