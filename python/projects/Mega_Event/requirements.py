validations = {
    "events":['Music Festival','Sports Match','Award Show','Exhibition'],
    "Ticket_types":{
        "Regular":160, 
        "Executive":280,
        "VIP":500
    }
}

discount_policies = [
    {"child": range(0, 12), "discount": 0.3},
    {"senior": range(65, 100), "discount": 0.25},
    {"others": range(12, 65), "discount": 0}
]

def get_discount(age):
    for policy in discount_policies:
        for key, age_range in policy.items():
            if key != "discount" and age in age_range:
                return policy["discount"]
    return 0  

print(get_discount(10))  # Example usage

def offer(n_tickets):
    if n_tickets >= 4:
        free_tickets = n_tickets // 4
        return free_tickets
    return 0

discount_day = "Saturday"
food={
    "snacks": [{"Popcorn":200}, {"Nachos":150}, {"Hot Dogs":120}, {"Soft Drinks":120}, {"Cold coffee":50}, {"Ice Cream":100}],
    "meals": ["Pizza", "Burgers", "Pasta", "Salads"]
    

}