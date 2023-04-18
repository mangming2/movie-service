from collections import namedtuple
import random
import queue_1
# 영화 클래스


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
    

class Cinema:
    def __init__ (self):
        self.movies = []
        self.reservation_queue = queue_1.Queue()
    
    def add_movie(self , movie):
        self.movies.append(movie)
    
    # 전체 영화 정보 제공  영화 제목, 상영관
    def get_all_movies(self):
        for movie in self.movies:
            print(movie.title)
            print(movie.theater.theater_num)
        
    # 영화 제목으로 영화 정보 제공
    def get_remain(self , movie):
        return movie.theater.remains
    
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

cinema.get_all_movies()

reserve_num= cinema.reserve("존윅4", 2, 3)
cinema.change(reserve_num, 3, 4)
cinema.cancellation(reserve_num)
cinema.get_all_movies()

title, n , m = input().split()
cinema.reserve(title, int(n), int(m))
    
    