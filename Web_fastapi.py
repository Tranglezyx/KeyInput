from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 模拟订单数据库
orders = []

# 定义请求数据模型
class OrderRequest(BaseModel):
    product_id: int
    quantity: int
    user_id: int

# 定义下单接口
@app.post('/order', summary="创建订单", response_description="订单信息")
async def create_order(order: OrderRequest):
    """
    创建订单接口
    - **product_id**: 商品ID
    - **quantity**: 数量
    - **user_id**: 用户ID
    """
    try:
        new_order = {
            "order_id": len(orders) + 1,
            "product_id": order.product_id,
            "quantity": order.quantity,
            "user_id": order.user_id
        }
        orders.append(new_order)
        return {"message": "订单创建成功", "order": new_order}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 先执行 pip install uvicorn命令
# 启动命令：uvicorn Wen_fastapi:app --host 0.0.0.0 --port 5000 --reload
