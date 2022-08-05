import sqlite3

def open_db(db_path):
    """Open the Database and ensure it exists.

    Args:
        db_path (str): The path to the database file.

    Returns:
        db (sqlite3.Connection): SQLite database connection
    """
    db = sqlite3.Connection(db_path)
    # Tables for end products
    # --------------------------------

    # Table for computers ready to sell, both ready to sell and in progress
    db.execute(
        """CREATE TABLE IF NOT EXISTS ComputerProducts(
            product_id TEXT PRIMARY KEY,
            brand TEXT,
            model TEXT,
            form_factor TEXT,
            processor TEXT,
            memory TEXT,
            graphics TEXT,
            storage TEXT,
            operating_system TEXT,
            connectivity TEXT,
            ports TEXT,
            display TEXT,
            other_features TEXT,
            removed_components TEXT,
            added_components TEXT,
            used_accessories TEXT,
            pre_sale_servicing TEXT,
            initial_system_cost REAL,
            initial_system_purchase_date TEXT,
            shipping_cost REAL,
            sale_price REAL,
            ready_to_sell INTEGER,
            sold INTEGER,
            sell_date TEXT)
        """
    )

    # Table for consistent/base service quotes
    db.execute(
        """CREATE TABLE IF NOT EXISTS ServiceQuotes(
        quote_id TEXT PRIMARY KEY,
        description TEXT,
        required_accessories TEXT,
        required_components TEXT,
        quote_price REAL)
        """
    )

    # Table for services provided to customers
    # customer_id points to a customer with more info
    # quote_id points to a quote with more info
    db.execute(
        """CREATE TABLE IF NOT EXISTS Services(
        case_id TEXT PRIMARY KEY,
        customer_id TEXT,
        quote_id TEXT,
        product_id TEXT,
        quote_date TEXT,
        deadline_date TEXT,
        status TEXT,
        completed_date TEXT)
        """
    )

    # Tables for storing costs
    # --------------------------------

    # Table for bought individual components
    db.execute(
        """CREATE TABLE IF NOT EXISTS Components(
            component_id TEXT PRIMARY KEY,
            type TEXT,
            brand TEXT,
            specs TEXT,
            pulled_from_product_id TEXT,
            total_cost REAL,
            quantity_purchased INTEGER,
            quantity_remaining INTEGER,
            purchase_date TEXT,
            purchase_location TEXT)
        """
    )

    # Table for bought accessories
    db.execute(
        """CREATE TABLE IF NOT EXISTS Accessories(
            accessory_purchase_id TEXT PRIMARY KEY,
            description TEXT,
            total_cost REAL,
            quantity_purchased INTEGER,
            quantity_remaining INTEGER,
            purchase_date TEXT,
            purchase_location TEXT)
        """
    )

    # Table for bought periodic services
    db.execute(
        """CREATE TABLE IF NOT EXISTS PeriodicServicesCosts(
            service_id TEXT PRIMARY KEY,
            description TEXT,
            payment_cost REAL,
            payment_frequency TEXT,
            payment_dates TEXT,
            active INTEGER,
            next_payment_date TEXT)
        """
    )

    # Table for bought one-time services
    db.execute(
        """CREATE TABLE IF NOT EXISTS OneTimeServiceCosts(
            service_id TEXT PRIMARY KEY,
            description TEXT,
            cost REAL,
            partner_id TEXT)
        """
    )

    # Tables for customers, partners, consultants, and business information
    # --------------------------------

    # Table for customer information
    db.execute(
        """CREATE TABLE IF NOT EXISTS Customers(
            customer_id TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            shipping_street_address TEXT,
            shipping_city TEXT,
            shipping_state_province TEXT,
            shipping_zip_code TEXT,
            billing_street_address TEXT,
            billing_city TEXT,
            billing_state_province TEXT,
            billing_zip_code TEXT,
            billing_shipping_same INTEGER)
        """
    )

    # Table for partners, consultants
    db.execute(
        """CREATE TABLE IF NOT EXISTS PartnersConsultants(
            partner_id TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            organization TEXT,
            active INTEGER)
        """
    )
