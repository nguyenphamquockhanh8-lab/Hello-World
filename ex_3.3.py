
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')


def giai_bai_2x2():
    print("--- ĐANG CHẠY LƯỚI 2X2 ---")
    def print_beams():
        do_twice(print_beam)
        print('+')
    def print_posts():
        do_twice(print_post)
        print('|')
    def print_row():
        print_beams()
        do_four(print_posts)
    
   
    do_twice(print_row)
    print_beams()


def giai_bai_4x4():
    print("\n--- ĐANG CHẠY LƯỚI 4X4 ---")
    def print_beams():
        do_four(print_beam)
        print('+')
    def print_posts():
        do_four(print_post)
        print('|')
    def print_row():
        print_beams()
        do_four(print_posts)
    
    
    do_four(print_row)
    print_beams()


if __name__ == "__main__":
    giai_bai_2x2()  
    giai_bai_4x4()  





