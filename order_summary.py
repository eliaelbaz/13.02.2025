def order_summary(*args, **kwargs):
    print("Order Summary:")
    print(f"Number of items: {len(args)}")
    for index, item in enumerate(args, start=1):
        print(f"  {index}. {item}")

    if "delivery_price" in kwargs:
        print(f"Delivery Price: {kwargs['delivery_price']}")
    else:
        print("No shipping")

    if "order_number" in kwargs:
        order_num = kwargs["order_number"]
        if 1 <= order_num <= 20:
            print(f"Order number {order_num} is valid (within 1–20).")
        else:
            print(f"Order number {order_num} is invalid (should be between 1 and 20).")
    else:
        print("Order number not provided.")

    handled_keys = {"delivery_price", "order_number"}
    for key, value in kwargs.items():
        if key not in handled_keys:
            print(f"{key}: {value}")

if __name__ == "__main__":
    order_summary(
        "Burger", "Fries", "Coke",
        customer_name="eliya elbaz",
        delivery_price=15,
        special_instructions="Extra ketchup",
        order_number=5
    )

    print("\n--- Another Order ---\n")

    order_summary(
        "Pizza", "Garlic Bread",
        customer_name="itay The teacher",
        special_instructions="No cheese",
        order_number=25
    )