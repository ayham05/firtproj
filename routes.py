from librarys import *
from models import *
from database import *

router = APIRouter()

@router.get("/products")
async def allProducts(sec:Session = Depends(get_session)):
    x = select(Products)
    ret = sec.exec(x).all() 
    return ret


@router.get("/item/{id}")
async def getid(id:int, resp:Response, sec : Session = Depends(get_session)):
    ret = sec.get(Products, id)
    if not ret:
        # raise HTTPException(status_code = 404, detail = "NOT FOUND")
        resp.status_code = status.HTTP_404_NOT_FOUND
        return {"Messege":"ERROR"}
    else:
        return ret


@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create(f:get_Product, sec:Session = Depends(get_session)):
    pp:Products = Products(f)
    sec.add(pp)
    sec.commit()
    sec.refresh(pp)
    return pp #* **Response:** `201 Created` with the newly created product object.??????????????????


@router.put("/products/{id}")
async def update(id:int ,f:get_Product, sec:Session = Depends(get_session)):
    x = sec.get(Products, id)
    if not x :
        raise HTTPException(status_code= 404, detail="NOT FOUND")
    else:
        x.name = f.name
        x.price = f.price
        x.stock = f.stock
        x.description = f.description
        sec.add(x)
        sec.commit()
        sec.refresh(x)
        return x
    

@router.delete("/products/{id}")
async def dele(id:int , sec:Session = Depends(get_session)):
    x = sec.get(Products, id)
    if not x :
        raise HTTPException(status_code= 404, detail="NOT FOUND")
    else:
        sec.delete(x)
        sec.commit()
        return {"messege":"item deleted"}
    

