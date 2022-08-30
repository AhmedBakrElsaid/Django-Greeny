
System :

        - products
        - accounts [activation:email]
        - orders / track order
        - coupons
        - payments
        - dashboard
        --------------------------------

        - celery / redis
        - cashing
        - optimization
        - django command
        - translation
        - ajax
        - docker
        - deploy [heroku - aws]
        ------------------------------
        APi
        Docs
        -------------------------------------------------------------


Products :
        - name 
        - sku
        - brand    * [name-img]
        - images   *
        - subtitle
        - description
        - tags     * package
        - price
        - flag [new - sale - feature] dropdown
        - quantity
        - reviews    * [user_id,rate[1-5],feedback,datetime]
        - category    * [name - img]


Orders :

        - status [received,processed,shipped,delivered]
        - user
        - id
        - total items
        - delivery time 
        - order time
        - total
        - sub_total


Order Details :

        - order id
        - product id
        - price
        - quantity
        - total

User :

        - address       *
        - name
        - email
        - image
        - phone_number *  
-------------------------------------------------------------------


- reusable Apps
- single Apps
- 3 Apps


