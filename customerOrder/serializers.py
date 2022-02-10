from rest_framework import serializers
from customerOrder.models import CustomerOrder

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerOrder
        fields='__all__' # all attributes
        # fields=('customerId','firstName','lastName','dateOfBirth','currencyBalance','pageVisitors') # each attributes
        