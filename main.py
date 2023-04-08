from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
from create_db import session, BusinessCardsModel

app = FastAPI()


# Шаблон создания визитки
class BusinessCard(BaseModel):

    company_name: str
    company_services_type: str
    company_description: str
    company_phone_number: str
    company_instagram: str | None
    company_telegram: str | None
    company_address: str
    company_website: str | None


class UpdateBusinessCard(BusinessCard):

    company_name: str | None
    company_services_type: str | None
    company_description: str | None
    company_phone_number: str | None
    company_instagram: str | None
    company_telegram: str | None
    company_address: str | None
    company_website: str | None


# Получение визитки по id
@app.get('/business_cards/{id}')
def get_business_card_by_id(id: int):

    # Запрос на поиск визитки по id
    business_card = session.query(BusinessCardsModel).get(id)
    # Если такой визитки по id нету
    if not business_card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"business card with id {id} wasn't found")
    
    return {'business_card_detail': business_card}


# Удаление визитки по её id
@app.delete('/business_cards/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_business_card(id: int):

    # Нахождение визитки
    business_card = session.query(BusinessCardsModel).get(id)
    # Если такой нету -> вызываем исключение
    if not business_card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"business card with id {id} wasn't found")
    # Удаляем визитку и сохраняем изменения
    session.delete(business_card)
    session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Обновить визитку
@app.put('/business_cards/{id}')
def update_business_card(id: int, business_card: UpdateBusinessCard):

    # Ищем визитку с id
    chosen_business_card = session.query(BusinessCardsModel).get(id)
    if not chosen_business_card:
        raise HTTPException(status_code=status. HTTP_404_NOT_FOUND,
                            detail=f"business card with id {id} wasn't found")
    # Делаем словарь -> в переменную update_business_card
    update_business_card = business_card.dict()

    # В цикле пробегаемся по измененым данным и изменяем их
    for k in update_business_card.keys():
        chosen_business_card.__dict__[k] = update_business_card[k]
    
    # Сохраняем значения
    session.commit()

    return {"updated_business_card": chosen_business_card}


#Получение всех визиток
@app.get('/business_cards')
def get_business_cards():

    # Получение списка всех обьектов бд
    all_business_cards = session.query(BusinessCardsModel).all()
    print(all_business_cards)
    
    return {'all_business_cards': all_business_cards}


# Создание визитки
@app.post('/business_cards', status_code=status.HTTP_201_CREATED)
def create_business_card(business_card: BusinessCard):

    business_card = business_card.dict()
    # Создание обьекта визитки
    new_business_card = BusinessCardsModel(company_name=business_card['company_name'],
                                           company_services_type=business_card['company_services_type'],
                                           company_description=business_card['company_description'],
                                           company_phone_number=business_card['company_phone_number'],
                                           company_instagram=business_card['company_instagram'],
                                           company_telegram=business_card['company_telegram'],
                                           company_address=business_card['company_address'],
                                           company_website=business_card['company_website'])
    # Добавление визитки в базу данных и сохранение изменений
    session.add(new_business_card)
    session.commit()
    
    return {'business_card_detail': business_card}
