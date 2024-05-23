from django.test import TestCase
from .models import Movie, Room, FeatureFilm, Ticket
from django.utils import timezone


# Create your tests here.
class CinemaTestCase(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            name="Harry Potter 1",
            director="J.K. Rowling",
            duration=120,
            synopsis="Something about wizards."
        )

        self.room = Room.objects.create(
            name="A",
            capacity=1000
        )

        self.feature_film = FeatureFilm.objects.create(
            movie=self.movie,
            room=self.room,
            start_date=timezone.now().date()
        )

        self.ticket = Ticket.objects.create(
            feature_film=self.feature_film,
            seat_number="3A",
            price=5.50
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.name, "Harry Potter 1")

    def test_room_creation(self):
        self.assertEqual(self.room.name, "A")

    def test_feature_film_creation(self):
        self.assertEqual(self.feature_film.movie.name, "Harry Potter 1")

    def test_feature_film_expired_date(self):
        self.assertGreaterEqual(timezone.now().date(), self.feature_film.start_date)

    def test_ticket_right_price(self):
        self.assertGreater(self.ticket.price, 0)

    def test_ticket_right_feature_film(self):
        self.assertNotEqual(self.ticket.feature_film, None)

    def test_ticket_right_seat_number(self):
        self.assertEqual(len(self.ticket.seat_number), 2)

    # def test_exceed_room_capacity(self):
    #     with self.assertRaises(Exception):  # Reemplaza Exception con la excepción específica que esperarías.
    #         for i in range(1, 1002):  # Supera la capacidad de la sala.
    #             Ticket.objects.create(
    #                 feature_film=self.feature_film,
    #                 seat_number=str(i),  # Asumiendo que cada asiento tiene un identificador único.
    #                 price=5.50
    #             )



