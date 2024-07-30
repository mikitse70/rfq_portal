import django
from django.db import models

from django.db import models


from django.contrib.auth.models import User



class QuotationRequest(models.Model):
    quotation_number= models.IntegerField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_place = models.CharField(max_length=255,null=True)
    delivery_term = models.CharField(max_length=255,null=True)
    specification = models.FileField(upload_to="uploads/request",null=True)
    boq = models.FileField(upload_to="uploads/request/",null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    modified_at = models.DateTimeField(auto_now=True)
    rfq_ref= models.IntegerField(null=False)
    deadline_date= models.DateTimeField(null=False)
    def __str__(self):
        return f"Quotation Request {self.quotation_number}"

class QuotationLine(models.Model):
    quotation_request = models.ForeignKey(QuotationRequest, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    
    book_type = models.CharField(max_length=100)
    line_number= models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f"Quotation Line{self.quotation_request.quotation_number} {self.line_number}"


class SupplierBid(models.Model):
    quotation_request = models.ForeignKey(QuotationRequest, on_delete=models.CASCADE)
    quotation_line = models.ForeignKey(QuotationLine, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    validity_date = models.DateField()
    payment = models.CharField(max_length=100)
    lead_time = models.IntegerField()
    file = models.FileField(upload_to="uploads/bids/")
    boq_total = models.FileField(upload_to="uploads/bids/")
    bid_status = models.CharField(default=0,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    vat=models.IntegerField()
    delivery_term = models.CharField(max_length=100, default='')
   

    def __str__(self):
        return f"Bid {self.id} by {self.user_id}"


