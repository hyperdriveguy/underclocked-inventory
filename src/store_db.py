import sqlite3
import json
from datetime import datetime, date


class DateList:

    def __init__(self, iso_date_list):
        self._internal_set = set(map(date.fromisoformat, remove_dups))

    def add(self, item: date):
        if item not in self._internal_set:
            self._internal_set.add(item)
    
    def remove(self, item: date):
        self._internal_set.remove(item)
    
    def in_order(self):
        return list(sorted(self._internal_set))
    
    def __sizeof__(self):
        return len(self._internal_set)

    def __str__(self):
        return str(self._internal_set)
    
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return json.dumps(list(self._internal_set))


def adapt_date_list(date_list):
    date_string_list = list(map(lambda x: x.isoformat(), date_list))
    return json.dumps(date_string_list)


def open_db(db_path):
    """Open the Database and ensure it exists.

    Args:
        db_path (str): The path to the database file.

    Returns:
        db (sqlite3.Connection): SQLite database connection
    """
    sqlite3.register_adapter(bool, int)
    sqlite3.register_converter('BOOL', lambda val: bool(int(val)))

    sqlite3.register_adapter(dict, json.dumps)
    sqlite3.register_adapter(list, json.dumps)
    sqlite3.register_adapter(tuple, json.dumps)
    sqlite3.register_converter('JSON', json.loads)
    sqlite3.register_converter('LIST', json.loads)

    sqlite3.register_adapter(date, lambda val: val.isoformat())
    sqlite3.register_converter('DATE', date.fromisoformat)

    sqlite3.register_adapter(datetime, lambda val: val.isoformat())
    sqlite3.register_converter('TIMESTAMP', datetime.fromisoformat)

    sqlite3.register_converter('DATELIST', lambda d: DateList(d))

    db = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)

    # Tables for end products
    # --------------------------------

    # Table for computers ready to sell, both ready to sell and in progress
    db.execute(
        """CREATE TABLE IF NOT EXISTS ComputerProducts(
            product_id TEXT PRIMARY KEY,
            brand TEXT,
            model TEXT,
            form_factor TEXT,
            processor JSON,
            memory JSON,
            graphics JSON,
            storage JSON,
            operating_system JSON,
            connectivity JSON,
            ports JSON,
            display JSON,
            other_features JSON,
            removed_components LIST,
            added_components LIST,
            used_accessories LIST,
            pre_sale_servicing LIST,
            initial_system_cost REAL,
            initial_system_purchase_date DATE,
            shipping_cost REAL,
            sale_price REAL,
            ready_to_sell BOOL,
            sold BOOL,
            sell_date DATE)
        """
    )

    # Table for consistent/base service quotes
    db.execute(
        """CREATE TABLE IF NOT EXISTS ServiceQuotes(
        quote_id TEXT PRIMARY KEY,
        description TEXT,
        required_accessories LIST,
        required_components LIST,
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
        outsourced_service_id TEXT,
        quote_date DATE,
        deadline_date DATE,
        status TEXT,
        completed_date DATE)
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
            purchase_date DATE,
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
            purchase_date DATE,
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
            payment_dates DATELIST,
            active BOOL,
            next_payment_date DATE)
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
            phone TEXT
            organization TEXT)
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
            active BOOL)
        """
    )
