# underclocked-inventory
Inventory System for the Underclocked Tech Company.

## Roadmap
- [ ] Store information in SQLite database
    - [ ] Computer and other retail assets
    - [ ] Other expenses (services, items, licenses, permits)
    - [ ] Preformed services
    - [ ] Previously sold items
    - [ ] Bids for items
    - [ ] Service quotes
    - [ ] Customer information
    - [ ] Invoices (point to file)
    - [ ] Automatic DB backup
    - [ ] DB verification (mdsum or shasum) and audit logs
    - [ ] Eventual transition to a different SQL database for network access
- [ ] Terminal UI
    - [ ] Input retail asset information
    - [ ] Input itemized expenses
    - [ ] Input services
    - [ ] Add customer information
    - [ ] View all retail assets via an overview
    - [ ] View individual information for all respective types
    - [ ] Fetch assets by product ID
    - [ ] Update existing information
    - [ ] Generate online store listing information
    - [ ] Mouse support
- [ ] Wordpress integration
    - [ ] Update status of sold or unsold retail products
    - [ ] Associate Wordpress account with a customer
    - [ ] Make products visible/invisible to customers
    - [ ] Syncronize products from inventory, including spec and price updates
- [ ] Multiuser backend
    - [ ] Seperate code for server and client side
    - [ ] Allow for multiple interface types (TUI, GUI, Web, Mobile)
    - [ ] Different user permissions
- [ ] Generate and print QR codes for product IDs
- [ ] Profit/loss overview
- [ ] Out of stock notifications
- [ ] Database tamper/corruption notification