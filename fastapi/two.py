from fastapi import FastAPI


app = FastAPI()

@app.get('/')# this is use to handle the request .
def index():
    return {"data":{"name":"sujal"}}

@app.get('blog/unpublished')

def unpublished():
    return {'data':'unpublished'}


@app.get('/blog/{id}')# id is to fetch the data dynamically
def show(id:int):
    return {'data':id}


@app.get('/about')
def About():
    return{'data':'about page'}




@app.get('/blog/{id}/comment')
def comment(id):
    return {'data':(id,"2")}

@app.get('/blog?limit=10&published=true')
def ind():
    # only get 10 published blogs
    return {'data':'blog list'}

@app.get('/blog/comment/{limit}')
def prac(limit):
    return {'data':f'{limit} will be published in db'}