import tkinter as tk
from tkinter import ttk, messagebox

from facade.pc_builder_facade import PCBuilderFacade


class PCBuilderGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PC Builder - Computer Configuration System")
        self.root.geometry("1100x750")
        self.root.minsize(1000, 700)

        self.facade = PCBuilderFacade()
        self.current_configuration = None

        self.configuration_types = {
            "Office PC": "office",
            "Gaming PC": "gaming",
            "Server PC": "server"
        }

        self.create_interface()
        self.refresh_catalog()

    def create_interface(self):
        self.root.configure(bg="#f4f6f8")

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TFrame",
            background="#f4f6f8"
        )

        style.configure(
            "TLabel",
            background="#f4f6f8",
            font=("Arial", 10)
        )

        style.configure(
            "Title.TLabel",
            font=("Arial", 24, "bold"),
            foreground="#1f2937",
            background="#f4f6f8"
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Arial", 11),
            foreground="#6b7280",
            background="#f4f6f8"
        )

        style.configure(
            "TLabelframe",
            background="#ffffff",
            borderwidth=1
        )

        style.configure(
            "TLabelframe.Label",
            font=("Arial", 11, "bold"),
            background="#ffffff",
            foreground="#1f2937"
        )

        style.configure(
            "TButton",
            font=("Arial", 10),
            padding=8
        )

        style.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=28
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        self.create_header()
        self.create_main_content()
        self.create_status_bar()

    def create_header(self):
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill="x", padx=25, pady=(20, 10))

        title_label = ttk.Label(
            header_frame,
            text="PC Builder",
            style="Title.TLabel"
        )
        title_label.pack()

        subtitle_label = ttk.Label(
            header_frame,
            text="Computer Configuration System",
            style="Subtitle.TLabel"
        )
        subtitle_label.pack(pady=(5, 0))

    def create_main_content(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=25, pady=15)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(0, weight=1)

        self.create_left_panel(main_frame)
        self.create_right_panel(main_frame)

    def create_left_panel(self, parent):
        left_frame = ttk.Frame(parent)
        left_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        left_frame.rowconfigure(1, weight=1)

        self.create_configuration_frame(left_frame)
        self.create_components_frame(left_frame)

    def create_configuration_frame(self, parent):
        configuration_frame = ttk.LabelFrame(
            parent,
            text="Base Configuration",
            padding=15
        )

        configuration_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            configuration_frame,
            text="Select computer type:"
        ).pack(anchor="w", pady=(0, 5))

        self.configuration_var = tk.StringVar()

        self.configuration_dropdown = ttk.Combobox(
            configuration_frame,
            textvariable=self.configuration_var,
            values=list(self.configuration_types.keys()),
            state="readonly"
        )

        self.configuration_dropdown.pack(
            fill="x",
            pady=(0, 10)
        )

        create_button = ttk.Button(
            configuration_frame,
            text="Create Configuration",
            command=self.create_configuration
        )

        create_button.pack(fill="x")

    def create_components_frame(self, parent):
        components_frame = ttk.LabelFrame(
            parent,
            text="Add Components",
            padding=15
        )

        components_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            components_frame,
            text="Select component:"
        ).pack(anchor="w", pady=(0, 5))

        self.component_var = tk.StringVar()

        self.component_dropdown = ttk.Combobox(
            components_frame,
            textvariable=self.component_var,
            state="readonly"
        )

        self.component_dropdown.pack(
            fill="x",
            pady=(0, 10)
        )

        add_component_button = ttk.Button(
            components_frame,
            text="Add Component",
            command=self.add_component
        )

        add_component_button.pack(fill="x")

        ttk.Separator(
            components_frame,
            orient="horizontal"
        ).pack(fill="x", pady=15)

        ttk.Label(
            components_frame,
            text="Update Component Price:"
        ).pack(anchor="w", pady=(0, 5))

        self.price_component_var = tk.StringVar()

        self.price_component_dropdown = ttk.Combobox(
            components_frame,
            textvariable=self.price_component_var,
            state="readonly"
        )

        self.price_component_dropdown.pack(
            fill="x",
            pady=(0, 10)
        )

        ttk.Label(
            components_frame,
            text="New price (EUR):"
        ).pack(anchor="w", pady=(0, 5))

        self.new_price_entry = ttk.Entry(
            components_frame
        )

        self.new_price_entry.pack(
            fill="x",
            pady=(0, 10)
        )

        update_price_button = ttk.Button(
            components_frame,
            text="Update Price",
            command=self.update_price
        )

        update_price_button.pack(fill="x")

        history_button = ttk.Button(
            components_frame,
            text="View Price History",
            command=self.show_price_history
        )

        history_button.pack(
            fill="x",
            pady=(10, 0)
        )

    def create_right_panel(self, parent):
        right_frame = ttk.Frame(parent)

        right_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        right_frame.rowconfigure(0, weight=2)
        right_frame.rowconfigure(1, weight=1)
        right_frame.columnconfigure(0, weight=1)

        self.create_configuration_display(right_frame)
        self.create_catalog_frame(right_frame)

    def create_configuration_display(self, parent):
        configuration_frame = ttk.LabelFrame(
            parent,
            text="Current Configuration",
            padding=15
        )

        configuration_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            pady=(0, 15)
        )

        configuration_frame.rowconfigure(0, weight=1)
        configuration_frame.columnconfigure(0, weight=1)

        self.configuration_text = tk.Text(
            configuration_frame,
            height=12,
            font=("Consolas", 11),
            wrap="word",
            state="disabled",
            background="#ffffff",
            relief="flat",
            padx=10,
            pady=10
        )

        self.configuration_text.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar = ttk.Scrollbar(
            configuration_frame,
            orient="vertical",
            command=self.configuration_text.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.configuration_text.configure(
            yscrollcommand=scrollbar.set
        )

    def create_catalog_frame(self, parent):
        catalog_frame = ttk.LabelFrame(
            parent,
            text="Component Catalog",
            padding=10
        )

        catalog_frame.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        catalog_frame.rowconfigure(0, weight=1)
        catalog_frame.columnconfigure(0, weight=1)

        columns = (
            "name",
            "category",
            "price",
            "performance"
        )

        self.catalog_tree = ttk.Treeview(
            catalog_frame,
            columns=columns,
            show="headings",
            height=5
        )

        self.catalog_tree.heading(
            "name",
            text="Component"
        )

        self.catalog_tree.heading(
            "category",
            text="Category"
        )

        self.catalog_tree.heading(
            "price",
            text="Price (EUR)"
        )

        self.catalog_tree.heading(
            "performance",
            text="Performance"
        )

        self.catalog_tree.column(
            "name",
            width=200
        )

        self.catalog_tree.column(
            "category",
            width=80,
            anchor="center"
        )

        self.catalog_tree.column(
            "price",
            width=100,
            anchor="center"
        )

        self.catalog_tree.column(
            "performance",
            width=100,
            anchor="center"
        )

        self.catalog_tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        catalog_scrollbar = ttk.Scrollbar(
            catalog_frame,
            orient="vertical",
            command=self.catalog_tree.yview
        )

        catalog_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.catalog_tree.configure(
            yscrollcommand=catalog_scrollbar.set
        )

        self.catalog_tree.bind(
            "<<TreeviewSelect>>",
            self.select_catalog_component
        )

    def create_status_bar(self):
        self.status_var = tk.StringVar(
            value="Ready. Select a base configuration."
        )

        status_label = ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief="sunken",
            anchor="w",
            padding=8
        )

        status_label.pack(
            fill="x",
            side="bottom"
        )

    def create_configuration(self):
        selected_configuration = self.configuration_var.get()

        if not selected_configuration:
            messagebox.showwarning(
                "Missing Configuration",
                "Please select a base configuration."
            )
            return

        computer_type = self.configuration_types[
            selected_configuration
        ]

        try:
            self.facade.create_computer(computer_type)

            self.current_configuration = selected_configuration

            self.refresh_configuration()

            self.status_var.set(
                f"{selected_configuration} created successfully."
            )

            messagebox.showinfo(
                "Success",
                f"{selected_configuration} was created successfully!"
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def add_component(self):
        component_name = self.component_var.get()

        if not component_name:
            messagebox.showwarning(
                "Missing Component",
                "Please select a component."
            )
            return

        try:
            self.facade.add_component(component_name)

            self.refresh_configuration()

            self.status_var.set(
                f"{component_name} added successfully."
            )

            messagebox.showinfo(
                "Success",
                f"{component_name} was added successfully!"
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def update_price(self):
        component_name = self.price_component_var.get()
        new_price_text = self.new_price_entry.get().strip()

        if not component_name:
            messagebox.showwarning(
                "Missing Component",
                "Please select a component."
            )
            return

        if not new_price_text:
            messagebox.showwarning(
                "Missing Price",
                "Please enter a new price."
            )
            return

        try:
            new_price = float(
                new_price_text.replace(",", ".")
            )

            if new_price <= 0:
                messagebox.showwarning(
                    "Invalid Price",
                    "Price must be greater than zero."
                )
                return

            self.facade.update_component_price(
                component_name,
                new_price
            )

            self.refresh_catalog()
            self.refresh_configuration()

            self.new_price_entry.delete(0, tk.END)

            self.status_var.set(
                f"Price of {component_name} updated successfully."
            )

            messagebox.showinfo(
                "Success",
                f"Price of {component_name} was updated to "
                f"{new_price:.2f} EUR."
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid numeric price."
            )

    def refresh_configuration(self):
        self.configuration_text.configure(
            state="normal"
        )

        self.configuration_text.delete(
            "1.0",
            tk.END
        )

        if self.current_configuration is None:
            self.configuration_text.insert(
                tk.END,
                "No configuration selected.\n\n"
                "Please select a base configuration "
                "and click Create Configuration."
            )

        else:
            configuration = self.facade.get_configuration()

            self.configuration_text.insert(
                tk.END,
                "COMPUTER CONFIGURATION\n"
                "==============================\n\n"
            )

            self.configuration_text.insert(
                tk.END,
                f"{configuration['description']}\n\n"
            )

            self.configuration_text.insert(
                tk.END,
                "TOTAL PRICE\n"
                "------------------------------\n"
            )

            self.configuration_text.insert(
                tk.END,
                f"{configuration['price']:.2f} EUR\n\n"
            )

            self.configuration_text.insert(
                tk.END,
                "PERFORMANCE\n"
                "------------------------------\n"
            )

            self.configuration_text.insert(
                tk.END,
                f"{configuration['performance']} points\n\n"
            )

            self.configuration_text.insert(
                tk.END,
                "STATUS\n"
                "------------------------------\n"
            )

            self.configuration_text.insert(
                tk.END,
                "Configuration ready."
            )

        self.configuration_text.configure(
            state="disabled"
        )

    def refresh_catalog(self):
        components = self.facade.get_available_components()

        self.catalog_tree.delete(
            *self.catalog_tree.get_children()
        )

        component_names = []

        for component_name, component in components.items():
            component_names.append(component_name)

            self.catalog_tree.insert(
                "",
                tk.END,
                iid=component_name,
                values=(
                    component.name,
                    component.category,
                    f"{component.price:.2f}",
                    component.performance_points
                )
            )

        self.component_dropdown.configure(
            values=component_names
        )

        self.price_component_dropdown.configure(
            values=component_names
        )

    def select_catalog_component(self, event):
        selected_item = self.catalog_tree.selection()

        if not selected_item:
            return

        component_name = selected_item[0]

        self.price_component_var.set(
            component_name
        )

    def show_price_history(self):
        history = self.facade.get_price_history()

        history_window = tk.Toplevel(self.root)

        history_window.title("Price History")
        history_window.geometry("600x400")
        history_window.resizable(False, False)

        history_text = tk.Text(
            history_window,
            font=("Consolas", 11),
            wrap="word",
            padx=15,
            pady=15
        )

        history_text.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        if not history:
            history_text.insert(
                tk.END,
                "No price changes have been recorded yet."
            )

        else:
            history_text.insert(
                tk.END,
                "PRICE HISTORY\n"
                "==============================\n\n"
            )

            for change in history:
                history_text.insert(
                    tk.END,
                    f"Component: {change['component']}\n"
                    f"Previous Price: "
                    f"{change['old_price']:.2f} EUR\n"
                    f"New Price: "
                    f"{change['new_price']:.2f} EUR\n"
                    "------------------------------\n"
                )

        history_text.configure(
            state="disabled"
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PCBuilderGUI()
    app.run()