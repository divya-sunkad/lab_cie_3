def vehicle_information(v_id,name,price,YOP):
    result=(
        f"vehicle id={v_id}/n"
        f"vehicle name={name}/n"
        f"vehicle price={price}/n"
        f"year of purchase={YOP}/n"
    )
if __name__=="__main__":
    v_id="v101"
    name="bullete"
    price=200000
    YOP=2006
print(vehicle_information(v_id,name,price,YOP))
