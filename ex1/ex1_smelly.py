class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

        # Step 2&3: Calculate total price and discount
        total_price = self.calculate_total_price(order["items"],order.get("discount_code"))

        # Step 4: Update inventory
        self.update_inventory(order["items"])
        
        # Step 5: Generate receipt
        receipt = self.generate_receipt(order["customer_id"],order["items"],total_price)

        # Step 6: Send confirmation email
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

        return receipt

    def calculate_total_price(self,items,discount_code):
        total_price = 0
        for item in items:
            total_price += item["price"] * item["quantity"]
            
        if discount_code == "SUMMER20":
            total_price *= 0.8  # 20% discount
        elif discount_code == "WELCOME10":
            total_price *= 0.9  # 10% discount

        return total_price
    
    def update_inventory(self, items):
        for item in items:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def generate_receipt(self, customer_id, items, total_price):
        receipt = f"Customer ID: {customer_id}\n"
        receipt += "Items:\n"
        for item in items:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"

        return receipt