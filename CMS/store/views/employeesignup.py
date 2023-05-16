from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.employee import Employee
from django.views import View


class EmpSignup(View):
    def get(self, request):
        return render(request, 'employeesignup.html')

    def post(self, request):
        print("hii")
        postData = request.POST
        # first_name = postData.get('firstname')
        # last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # address = postData.get('address')
        # city = postData.get('city')
        # gender = postData.get('gender')
        # dob = postData.get('dob')



        # validation
        value = {
            # 'first_name': first_name,
            # 'last_name': last_name,
            'phone': phone,
            'email': email,
            'password':password
            # 'address' : address,
            # 'city' : city,
            # 'gender':gender,
            # 'dob':dob
        }
        error_message = None

        customer = Employee(
                            # first_name=first_name,
                            # last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password
                            # ,address=address,
                            # city=city,
                            # gender=gender,
                            # dob=dob
                            )
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(
                # first_name, last_name,
                phone, email, password,)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('empdash')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'employeesignup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.email):
            error_message = "email Required !!"
        # elif len(customer.first_name) < 4:
        #     error_message = 'First Name must be 4 char long or more'
        # elif not customer.last_name:
        #     error_message = 'Last Name Required'
        # elif len(customer.last_name) < 4:
        #     error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
