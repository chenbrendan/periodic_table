import requests

def get_element_info(query):
    """
    Fetch element info from the periodic table API.
    Query can be an element's symbol or name.
    Returns element data as JSON.
    """
    url = f"https://neelpatel05.pythonanywhere.com/element/atomicname?atomicname={query.capitalize()}"
    response = requests.get(url)

    # If searching by name fails, try symbol
    if response.status_code != 200 or not response.text:
        url = f"https://neelpatel05.pythonanywhere.com/element/symbol?symbol={query.capitalize()}"
        response = requests.get(url)

    if response.status_code != 200 or not response.text:
        return None

    return response.json()


def display_element_info(data):
    """Prints element info in a nicely formatted style."""
    print("\n--- Element Information ---")
    print(f"{'Atomic Number:':20} {data.get('atomicNumber')}")
    print(f"{'Symbol:':20} {data.get('symbol')}")
    print(f"{'Name:':20} {data.get('name')}")
    print(f"{'Atomic Mass:':20} {data.get('atomicMass')}")
    print(f"{'Electron Config:':20} {data.get('electronicConfiguration')}")
    print(f"{'Group Block:':20} {data.get('groupBlock')}")
    print(f"{'Standard State:':20} {data.get('standardState')}")
    print(f"{'Melting Point (°C):':20} {data.get('meltingPoint')}")
    print(f"{'Boiling Point (°C):':20} {data.get('boilingPoint')}")
    print(f"{'Density (g/cm³):':20} {data.get('density')}")
    print(f"{'Year of Discovery:':20} {data.get('yearDiscovered')}")
    print("------------------------------\n")


if __name__ == "__main__":
    print("🌐 Live Periodic Table Lookup")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Enter element name or symbol: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        data = get_element_info(query)
        if data:
            display_element_info(data)
        else:
            print(f"❌ Could not fetch data for '{query}'.\n")
