![](https://github.com/varnitsingh/amazon-Flash-Sale/images/flashSale.jpg)
# Amazon Flash Sale Autobuy Tool
Web Automation tool for adding products to cart automatically during Flash sales

## Example
    >#Example on how to add more accounts.
    >add another process name for example third_process
    >third_process = Process(target=add_to_cart,args=['account_email@gmail.com','password','product_link'])
    >third_process.start()
    >third_process.join()
