import math 
r=5
volume= (4/3) * math.pi * r ** 3
print(f"The tich cua hinh cau la: {volume:.2f}")
 
cover_price = 24.95
discount = 0.40
quantity = 60
discounted_price = cover_price * (1 - discount)
total_book_cost = discounted_price * quantity
shipping_cost = 3 + (quantity - 1) * 0.75
total_wholesale_cost = total_book_cost + shipping_cost
print(f"Tổng chi phí nhập 60 cuốn sách là: ${total_wholesale_cost:.2f}")

start_time_seconds = (6 * 3600) + (52 *60)
easy_pace_seconds = ( 8 * 60) +15
tempo_pace_seconds =(7 * 60) +12
total_run_time = (easy_pace_seconds * 1) + (tempo_pace_seconds *3) + (easy_pace_seconds * 1)
end_time_seconds = start_time_seconds +total_run_time
end_hour = end_time_seconds // 3600
end_minute = (end_time_seconds% 3600) //60
end_second= end_time_seconds % 60
print(f"Ve nha an sang luc: {end_hour}:{end_minute:02d}:{end_second:02d} AM")