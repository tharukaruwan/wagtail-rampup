from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__' # all attributes
        # fields=('customerId','firstName','lastName','dateOfBirth','currencyBalance','pageVisitors') # each attributes
        