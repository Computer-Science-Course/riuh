"""Order controllers."""

from flask.views import MethodView
from flask_smorest import Blueprint

from schemas.order import (
    CreateOrderSchema,
    UpdateOrderSchema,
    ViewOrderSchema,
)
from services.order import (
    OrderService,
)

blp = Blueprint('Order', __name__, description='Opretations on Orders.')

@blp.route('/order/<int:order_id>')
class Order(MethodView):
    """Controllers for specific order."""

    @blp.response(200, ViewOrderSchema)
    def get(self, order_id):
        """
        Get and order by its ID.

        :param int order_id: Order ID.

        :return ViewOrderSchema: Order.
        """

        service: OrderService = OrderService()
        return service.get_by_id(order_id)

    @blp.arguments(UpdateOrderSchema)
    @blp.response(200, ViewOrderSchema)
    def put(self, order_data, order_id):
        """
        Update an order.

        :request UpdateOrderSchema order_data: Order to be updated.
        :param int order_id: Order ID.

        :return ViewOrderSchema: Order.
        """

        service: OrderService = OrderService()
        return service.update(id=order_id, **order_data)


    @blp.response(200)
    def delete(self, order_id):
        """
        Delete a order.

        :param int order_id: Order ID.
        """

        service: OrderService = OrderService()
        return service.delete(order_id)




@blp.route('/order')
class OrderGeneral(MethodView):
    """Controllers fro general orders."""

    @blp.response(200, ViewOrderSchema(many=True))
    def get(self):
        """
        Get all orders.

        :return list: List of Orders.
        """

        service: OrderService = OrderService()
        return service.get_all()


    @blp.arguments(CreateOrderSchema)
    @blp.response(200, ViewOrderSchema)
    def post(self, order_data):
        """
        Create a new order.

        :return ViewOderSchema: Order to be stored.
        """

        service: OrderService = OrderService()
        return service.create(**order_data)
