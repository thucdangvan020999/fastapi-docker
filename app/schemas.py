from typing import List, Dict
from fastapi import Query
from pydantic import BaseModel, validator


class TableScore(BaseModel):
    # subject : List[str] = []
    # score : List[float] = []
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "subject": ['Calculas', 'Python ', 'Introduction to DS'],
    #             "score" :[9,8.5,6]
    #         }
    #     }    

    Dict[List[str], List[float]]
    class Config:
        schema_extra = {
            "example": {
                'Calculas' : '10',
                'Python' : '9',
                'OOP' : '8.5'
            }
        }  
class Text(BaseModel):
    text: str = Query(None, min_length=1)

class PredictPayloadCourse(BaseModel):
    texts: List[Text]

    @validator("texts")
    def list_must_not_be_empty(cls, value):
        if not len(value):
            raise ValueError("List of texts to classify cannot be empty.")
        return value
    
    
    class Config:
        schema_extra = {
            "example": {
                "texts": [
                    {"text": 'By the end of this Specialization, you will be ready to design NLP applications that perform question-answering and sentiment analysis, create tools to translate languages and summarize text, and even build chatbots. These and other NLP applications are going to be at the forefront of the coming transformation to an AI-powered future.'}
                ]
            }
        }

class PredictPayloadJB(BaseModel):
    texts: List[Text]

    @validator("texts")
    def list_must_not_be_empty(cls, value):
        if not len(value):
            raise ValueError("List of texts to classify cannot be empty.")
        return value
    
    
    class Config:
        schema_extra = {
            "example": {
                "texts": [
                    {"text": "Strong communication and interpersonal skills Solid understanding of Python or C/C++, programming techniques, and software development Passionate about presenting to technical audiences and generating content for developers"}
                ]
            }
        }