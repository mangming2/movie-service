from collections import namedtuple
import random
import queue_1




# 상영관 클래스
class Theater:
    def __init__ (self, theater_num , row , col):
        self.theater_num = theater_num
        self.row = row
        self.col = col
        self.seats=[[False]*col for _ in range(row)]
        self.remains = row*col
    
    def show_remains(self):
       for i in range(self.row):
           for j in range(self.col):
               if self.seats[i][j] == False:
                   print("O", end="")
               else:
                   print("X", end="")
           print()
        
   
# 영화 클래스     
class Movie:
    def __init__(self, title , theater):
        self.title = title
        self.theater = theater

class Reservation:
    def __init__ (self, movie , row , col):
        self.movie = movie
        self.row = row
        self.col = col
        self.reservation_num = random.randint(1000,9999)
    

#영화관 클래스
class Cinema:
    def __init__ (self):
        self.movies = []
        self.reservation_queue = queue_1.Queue()
    
    def add_movie(self , movie):
        self.movies.append(movie)
    
    # 전체 영화 정보 제공  영화 제목, 상영관
    def get_all_movies(self):
        for movie in self.movies:
            print("영화 제목: ", movie.title)
            print("상영관: ", movie.theater.theater_num)
        
    # 영화 제목으로 영화 정보 제공
    def get_remain(self , title):
        for movie in self.movies:
            if movie.title == title:
                print("잔여 좌석 : 총" ,  movie.theater.remains)
                movie.theater.show_remains()
                return movie.theater.remains
        return -1
    
    # 예약
    def reserve(self , title , row , col):
        for i in self.movies:
            if i.title == title:
                movie = i
                break
        if movie.theater.seats[row][col] == False:
            movie.theater.seats[row][col] = True
            movie.theater.remains -= 1
            reservation = Reservation(movie , row , col)
            self.reservation_queue.enqueue(reservation)
            print("예약완료: " , reservation.reservation_num)
            movie.theater.show_remains()
            return reservation.reservation_num
        elif movie.theater.seats[row][col] == True:
            print("이미 예약된 자리입니다.")
        elif movie.theater.remains == 0:
            print("예약 가능한 자리가 없습니다.")
    
    # 예약 취소
    def cancellation (self , reservation_num):
        if self.reservation_queue.is_empty():
            return False
        else:
            while not self.reservation_queue.is_empty():
                reservation = self.reservation_queue.dequeue()
                if reservation.reservation_num == reservation_num:
                    reservation.movie.theater.seats[reservation.row][reservation.col] = False
                    reservation.movie.theater.remains += 1
                    print("예약취소: " , reservation.reservation_num)
                    reservation.movie.theater.show_remains()
                    return True
                else:
                    self.reservation_queue.enqueue(reservation)
            return False
    
    # 예약 변경
    def change(self , reservation_num , row , col):
        if self.reservation_queue.is_empty():
            return False
        else:
            while not self.reservation_queue.is_empty():
                reservation = self.reservation_queue.dequeue()
                if reservation.reservation_num == reservation_num:
                    reservation.movie.theater.seats[reservation.row][reservation.col] = False
                    reservation.movie.theater.seats[row][col] = True
                    reservation.row = row
                    reservation.col = col
                    print("예약변경: " , reservation.reservation_num)
                    reservation.movie.theater.show_remains()
                    self.reservation_queue.enqueue(reservation)
                    return True
                else:
                    self.reservation_queue.enqueue(reservation)
            return False
    
    
    
cinema = Cinema()
theater1 = Theater(1, 5, 6)
theater2 = Theater(4, 6, 7)
theater3 = Theater(9, 7, 8)

john_wick = Movie("존윅4", theater1)
rebound = Movie("리바운드", theater2)
killing_romance = Movie("킬링 로맨스", theater3)

cinema.add_movie(john_wick)
cinema.add_movie(rebound)
cinema.add_movie(killing_romance)

print("1. 영화 정보 제공")
cinema.get_all_movies()

print("2. 예매 / 취소 / 변경 작업 요청 ")
print("3. 영화 예매 처리 기능 - 영화 제목 , 자리, 예매번호 저장")
reserve_num= cinema.reserve("존윅4", 2, 3)

print("5. 예매 변경 처리 기능 - 큐에서 예매번호 찾아서 변경처리")
cinema.change(reserve_num, 3, 4)

print ("4. 예매 취소 처리 기능 - 큐에서 예매번호 찾아서 취소처리")
cinema.cancellation(reserve_num)
cinema.get_all_movies()

reserve_num2 = cinema.reserve("존윅4", 2, 3)

print("6. 잔여 좌석 확인 기능")
cinema.get_remain("존윅4")

print("중복된 예매 정보일 경우")
reserve_num2 = cinema.reserve("존윅4", 2, 3)

while(True):
    print("원하시는 작업을 선택하세요")
    print("1. 예매 , 2. 취소 , 3. 변경 , 4. 잔여좌석 확인, 5. 종료")
    num1 = int(input())

    if num1 == 1:
        print("영화 제목, 좌석 행 , 좌석 열 을 입력하세요")
        title, n , m = input().split()
        cinema.reserve(title, int(n), int(m))  
    elif num1 == 2:
        print("예매번호를 입력하세요")
        reserve_num = int(input())
        cinema.cancellation(reserve_num)
    elif num1==3:
        print("예매번호, 좌석 행 , 좌석 열 을 입력하세요")
        reserve_num, n , m = map(int,input().split())
        cinema.change(reserve_num, int(n), int(m))
    elif num1==4:
        print("영화 제목을 입력하세요")
        title = input()
        cinema.get_remain(title)
    elif num1==5:
        break
    




    
    