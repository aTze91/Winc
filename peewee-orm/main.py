from asyncio.windows_events import NULL
from datetime import datetime
from hashlib import new
from select import select
from unittest import result
import models
import peewee
from typing import List
from models import Dish, DishIngredient, db, Ingredient, Rating, Restaurant

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    query = (Dish
             .select()
             .order_by(Dish.price_in_cents))
    return query[0]


def vegetarian_dishes() -> List[models.Dish]:
    query = DishIngredient\
            .select(DishIngredient, Dish, Ingredient)\
            .join(Ingredient)\
            .switch(DishIngredient)\
            .join(Dish)\
            .filter((Ingredient.is_vegetarian == False))\
            .group_by(Dish.name)\
            .objects()
    l = []
    result =[]
    for dish in query:
        l.append(dish.name)
    for dish in Dish.select(Dish).objects():
        if dish.name not in l:
            result.append(dish)
    return result

def vegan_dishes() -> List[models.Dish]:
    query = DishIngredient\
            .select(DishIngredient, Dish, Ingredient)\
            .join(Ingredient)\
            .switch(DishIngredient)\
            .join(Dish)\
            .filter((Ingredient.is_vegan == False))\
            .group_by(Dish.name)\
            .objects()
    l = []
    result =[]
    for dish in query:
        l.append(dish.name)
    for dish in Dish.select(Dish).objects():
        if dish.name not in l:
            result.append(dish)
    return result
def best_average_rating() -> models.Restaurant:
    query = (Restaurant
             .select(Restaurant, Rating)
             .join(Rating)
             .where(Restaurant.name == Rating.restaurant.name)
             .order_by(Rating.rating))
    return query


def add_rating_to_restaurant() -> None:
    rating = Rating(restaurant = 1, rating = 9, comment = 'new rating')
    rating.save()
    return rating


def dinner_date_possible() -> List[models.Restaurant]:
    open_restaurants = Restaurant.select(Restaurant.id)\
                      .filter((Restaurant.opening_time.hour <= 19)&\
                              (Restaurant.closing_time.hour >= 19))\
                      .objects()
    vegan_restaurants = []
    for dish in vegan_dishes():
        vegan_restaurants.append(dish.served_at)
    result = Restaurant.select()\
                       .filter((Restaurant.id << open_restaurants)\
                       &(Restaurant.id << vegan_restaurants))\
                       .objects()
    return result


def add_dish_to_menu() -> models.Dish:
    new_ingeredients = [
        {'name': 'cheese', 'is_vegetarian': True, 'is_vegan': False, 'is_glutenfree': True},
        {'name': 'honing', 'is_vegetarian': True, 'is_vegan': True, 'is_glutenfree': True},
        {'name': 'sla', 'is_vegetarian': True, 'is_vegan': True, 'is_glutenfree': True}
    ]
    new_dish = Dish(name= 'cheese sla', served_at=2, price_in_cents=500)
    new_dish.save()
    new_ids = []
    for ingredient in new_ingeredients:
        new_ingredient, created = Ingredient.get_or_create(name=ingredient['name'], defaults=ingredient)
        new_ids.append(new_ingredient.id)
    for x in new_ids:
        new_dish.ingredients.add(Ingredient.get(Ingredient.id==x))
    new_dish.save()
    return new_dish
