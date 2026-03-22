res_open=True
table_free=True
menu_card_there=False
if res_open:
    print("Welcome to our place")
    if table_free:
        print("Please take ur seat")
        if menu_card_there:
            print("Take ur menu")
        else:
            print("wait")
    else:
        print("wait for the next round")
else:
    print("Closed")