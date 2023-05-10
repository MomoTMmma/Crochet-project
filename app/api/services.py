from flask import jsonify

def get_Product():
    product = [
        {
            'product_id' : 1,
            'title' : 'Flower bag',
            'price' : 24.99,
            'description' : 'Hand crochet purse with a hand sewn in cotton lining',
            'category' : 'bags',
        },
        {
            'product_id' : 2,
            'title' : 'Steering Wheel Cover',
            'price' : 15.99,
            'description' : 'Blue with white daisys. Made with 100 percent acrylic yarn. Great for protecting your steering wheel from the sun!',
            'category' : 'accessories'
        },
        {
            'product_id' : 3,
            'title' : 'Steering Wheel Cover',
            'price' : 15.99,
            'description' : 'Red with sunflowers. Made with 100 percent acrylic yarn. Great for protecting your steering wheel from the sun!',
            'category' : 'accessories'
        }
    ]

    return ({'product': product})


