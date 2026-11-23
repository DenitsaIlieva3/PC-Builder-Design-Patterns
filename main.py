
from facade.pc_builder_facade import PCBuilderFacade


def display_menu():

    print("\n==============================")
    print("         PC BUILDER")
    print("==============================")
    print("1. Create computer")
    print("2. Add component")
    print("3. View configuration")
    print("4. Update component price")
    print("5. View price history")
    print("6. Exit")

    


def main():

    facade = PCBuilderFacade()

    while True:

        display_menu()

        choice = input("Choose an option (1-6): ")

        
        if choice == "1":
            print("\nSELECT COMPUTER TYPE")
            print("1. Office PC")
            print("2. Gaming PC")
            print("3. Server PC")

            computer_choice = input("Choose computer type (1-3): ")

            if computer_choice == "1":
                facade.create_computer("office")
                print("Office PC created successfully!")

            elif computer_choice == "2":
                facade.create_computer("gaming")
                print("Gaming PC created successfully!")

            elif computer_choice == "3":
                facade.create_computer("server")
                print("Server PC created successfully!")

            else:
                print("Invalid computer type!")


        
        
        elif choice == "2":

            components = facade.get_available_components()

            print("\nAVAILABLE COMPONENTS:")
            print("==============================")

            for number, component in enumerate(components.values(), start=1):
                print(
                    f"{number}. {component.name} - "
                    f"{component.price:.2f} EUR"
                )

            print("==============================")

            component_choice = input("Choose component (1-3): ")

            try:
                if component_choice == "1":
                    facade.add_component("Kingston Fury 32GB")
                    print("RAM added successfully!")

                elif component_choice == "2":
                    facade.add_component("Samsung 990 PRO 1TB")
                    print("SSD added successfully!")

                elif component_choice == "3":
                    facade.add_component("NVIDIA RTX 4070")
                    print("GPU added successfully!")

                else:
                    print("Invalid component choice!")

            except ValueError as error:
                print(f"\nError: {error}")


        
        elif choice == "3":

            try:
                configuration = facade.get_configuration()

                print("\n==============================")
                print("    CURRENT CONFIGURATION")
                print("==============================")
                print(configuration["description"])
                print(f"Total price: {configuration['price']:.2f} EUR")
                print(f"Performance: {configuration['performance']} points")
                print("==============================")

            except ValueError as error:
                print(f"\nError: {error}")


        
        elif choice == "4":

            components = facade.get_available_components()

            print("\nUPDATE COMPONENT PRICE")
            print("==============================")

            for number, component in enumerate(components.values(), start=1):
                print(
                    f"{number}. {component.name} - "
                    f"{component.price:.2f} EUR"
                )

            print("==============================")

            component_choice = input("Choose component (1-3): ")

            if component_choice == "1":
                component_name = "Kingston Fury 32GB"

            elif component_choice == "2":
                component_name = "Samsung 990 PRO 1TB"

            elif component_choice == "3":
                component_name = "NVIDIA RTX 4070"

            else:
                print("Invalid component choice!")
                continue

            try:
                new_price = float(input("Enter new price (EUR): "))

                if new_price <= 0:
                    print("Price must be greater than zero!")
                    continue

                facade.update_component_price(component_name, new_price)

            except ValueError:
                print("Please enter a valid number!")


        
        elif choice == "5":

            history = facade.get_price_history()

            print("\n==============================")
            print("         PRICE HISTORY")
            print("==============================")

            if not history:
                print("No price changes recorded.")

            else:
                for entry in history:
                    print(f"Component: {entry['component']}")
                    print(f"Old price: {entry['old_price']:.2f} EUR")
                    print(f"New price: {entry['new_price']:.2f} EUR")
                    print("------------------------------")


        elif choice == "6":
            print("\nThank you for using PC Builder!")
            break

        else:
            print("\nInvalid choice! Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
