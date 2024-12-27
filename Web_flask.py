from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟订单数据库
orders = []

@app.route('/order', methods=['POST'])
def create_order():
    """
    下单接口
    请求方法: POST
    请求参数: JSON ({"product_id": 1, "quantity": 2, "user_id": 123})
    返回: 订单确认信息
    """
    try:
        # 获取 JSON 数据
        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        user_id = data.get('user_id')

        # 参数校验
        if not all([product_id, quantity, user_id]):
            return jsonify({"error": "缺少必要参数"}), 400

        # 创建订单
        order = {
            "order_id": len(orders) + 1,
            "product_id": product_id,
            "quantity": quantity,
            "user_id": user_id
        }
        orders.append(order)

        return jsonify({"message": "订单创建成功", "order": order}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
