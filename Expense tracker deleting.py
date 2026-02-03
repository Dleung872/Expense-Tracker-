import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        """Initialize expense tracker"""
        self.filename = filename
        self.expenses = self.load_expenses()
        self.next_id = self.get_next_id()
    
    def load_expenses(self):
        """Load expense data from JSON file"""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_expenses(self):
        """Save expense data to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)
    
    def get_next_id(self):
        """Get next available ID"""
        if self.expenses:
            return max(int(key) for key in self.expenses.keys()) + 1
        return 1
    
    def filter_expenses_by_category(self, category):
        """
        Filter expenses by category
        Args:
            category: Category name to filter
        Returns:
            Dictionary of matching expenses
        """
        filtered = {}
        if not self.expenses:
            print("⚠️  No expense records found!")
            return filtered
        
        if not category:
            print("⚠️  Please enter a category name!")
            return filtered
        
        for exp_id, expense in self.expenses.items():
            if expense.get('category', '').lower() == category.lower():
                filtered[exp_id] = expense
        
        if not filtered:
            print(f"📭  No expenses found for category '{category}'")
        else:
            print(f"📋  Found {len(filtered)} expenses in category '{category}'")
        
        return filtered
    
    def filter_expenses_by_date_range(self, start_date=None, end_date=None):
        """
        Filter expenses by date range
        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
        Returns:
            Dictionary of matching expenses
        """
        filtered = {}
        if not self.expenses:
            print("⚠️  No expense records found!")
            return filtered
        
        try:
            if start_date:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
            if end_date:
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("❌  Invalid date format! Please use YYYY-MM-DD format")
            return filtered
        
        for exp_id, expense in self.expenses.items():
            exp_date_str = expense.get('date', '')
            try:
                exp_date = datetime.strptime(exp_date_str, "%Y-%m-%d")
                
                match = True
                if start_date and exp_date < start_date:
                    match = False
                if end_date and exp_date > end_date:
                    match = False
                
                if match:
                    filtered[exp_id] = expense
            except ValueError:
                continue
        
        if not filtered:
            print(f"📭  No expenses found in the specified date range")
            return filtered
        
        print(f"📋  Found {len(filtered)} expenses in the specified date range")
        return filtered
    
    def filter_expenses_by_amount_range(self, min_amount=None, max_amount=None):
        """
        Filter expenses by amount range
        Args:
            min_amount: Minimum amount
            max_amount: Maximum amount
        Returns:
            Dictionary of matching expenses
        """
        filtered = {}
        if not self.expenses:
            print("⚠️  No expense records found!")
            return filtered
        
        try:
            min_amount = float(min_amount) if min_amount else None
            max_amount = float(max_amount) if max_amount else None
        except ValueError:
            print("❌  Invalid amount format! Please enter valid numbers")
            return filtered
        
        for exp_id, expense in self.expenses.items():
            try:
                amount = float(expense.get('amount', 0))
                
                match = True
                if min_amount is not None and amount < min_amount:
                    match = False
                if max_amount is not None and amount > max_amount:
                    match = False
                
                if match:
                    filtered[exp_id] = expense
            except ValueError:
                continue
        
        if not filtered:
            print(f"📭  No expenses found in the specified amount range")
            return filtered
        
        print(f"📋  Found {len(filtered)} expenses in the specified amount range")
        return filtered
    
    def filter_expenses_by_multiple_criteria(self, category=None, start_date=None, end_date=None, min_amount=None, max_amount=None):
        """
        Filter expenses by multiple criteria
        Args:
            category: Category to filter (optional)
            start_date: Start date (optional)
            end_date: End date (optional)
            min_amount: Minimum amount (optional)
            max_amount: Maximum amount (optional)
        Returns:
            Dictionary of matching expenses
        """
        filtered = {}
        if not self.expenses:
            print("⚠️  No expense records found!")
            return filtered
        
        # Convert dates to datetime objects if provided
        try:
            start_date_dt = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
            end_date_dt = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
        except ValueError:
            print("❌  Invalid date format! Please use YYYY-MM-DD format")
            return filtered
        
        # Convert amounts to float if provided
        try:
            min_amount_val = float(min_amount) if min_amount else None
            max_amount_val = float(max_amount) if max_amount else None
        except ValueError:
            print("❌  Invalid amount format! Please enter valid numbers")
            return filtered
        
        for exp_id, expense in self.expenses.items():
            match = True
            
            # Check category
            if category and expense.get('category', '').lower() != category.lower():
                match = False
            
            # Check date range
            if match and (start_date_dt or end_date_dt):
                exp_date_str = expense.get('date', '')
                try:
                    exp_date = datetime.strptime(exp_date_str, "%Y-%m-%d")
                    if start_date_dt and exp_date < start_date_dt:
                        match = False
                    if end_date_dt and exp_date > end_date_dt:
                        match = False
                except ValueError:
                    match = False
            
            # Check amount range
            if match and (min_amount_val is not None or max_amount_val is not None):
                try:
                    amount = float(expense.get('amount', 0))
                    if min_amount_val is not None and amount < min_amount_val:
                        match = False
                    if max_amount_val is not None and amount > max_amount_val:
                        match = False
                except ValueError:
                    match = False
            
            if match:
                filtered[exp_id] = expense
        
        if not filtered:
            print("📭  No expenses match all the specified criteria")
        else:
            print(f"📋  Found {len(filtered)} expenses matching all criteria")
        
        return filtered
    
    def display_filtered_expenses(self, filtered_expenses):
        """Display filtered expenses"""
        if not filtered_expenses:
            print("No matching expense records found")
            return
        
        print("\n" + "="*60)
        print("📊 FILTER RESULTS:")
        print("="*60)
        for exp_id, expense in filtered_expenses.items():
            self.display_single_expense(exp_id, expense)
        print("="*60)
    
    def display_single_expense(self, exp_id, expense):
        """Display a single expense"""
        print(f"ID: {exp_id}")
        print(f"  Category: {expense.get('category', 'N/A')}")
        print(f"  Amount: ${expense.get('amount', 0):.2f}")
        print(f"  Date: {expense.get('date', 'N/A')}")
        if 'description' in expense:
            print(f"  Description: {expense.get('description', '')}")
        print("-" * 40)
    
    def delete_expense_by_id(self, expense_id):
        """
        Delete expense by ID
        Args:
            expense_id: ID of expense to delete
        Returns:
            bool: True if deletion was successful
        """
        if expense_id in self.expenses:
            deleted_expense = self.expenses.pop(expense_id)
            self.save_expenses()
            print(f"✅  Successfully deleted expense (ID: {expense_id})")
            print(f"   Category: {deleted_expense.get('category')}")
            print(f"   Amount: ${deleted_expense.get('amount'):.2f}")
            print(f"   Date: {deleted_expense.get('date')}")
            return True
        else:
            print(f"❌  No expense found with ID '{expense_id}'")
            return False
    
    def delete_expenses_by_category(self, category):
        """
        Delete all expenses in a category
        Args:
            category: Category to delete
        Returns:
            int: Number of expenses deleted
        """
        if not self.expenses:
            print("⚠️  No expense records found!")
            return 0
        
        expenses_to_delete = []
        for exp_id, expense in self.expenses.items():
            if expense.get('category', '').lower() == category.lower():
                expenses_to_delete.append(exp_id)
        
        if not expenses_to_delete:
            print(f"📭  No expenses found for category '{category}'")
            return 0
        
        print(f"⚠️  Are you sure you want to delete {len(expenses_to_delete)} expenses in category '{category}'?")
        confirmation = input("Type 'yes' to confirm: ").strip().lower()
        
        if confirmation == 'yes':
            deleted_count = 0
            for exp_id in expenses_to_delete:
                del self.expenses[exp_id]
                deleted_count += 1
            self.save_expenses()
            print(f"✅  Successfully deleted {deleted_count} expenses")
            return deleted_count
        else:
            print("❌  Deletion cancelled")
            return 0
    
    def delete_expenses_by_date(self, date):
        """
        Delete all expenses on a specific date
        Args:
            date: Date to delete (YYYY-MM-DD)
        Returns:
            int: Number of expenses deleted
        """
        if not self.expenses:
            print("⚠️  No expense records found!")
            return 0
        
        try:
            target_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("❌  Invalid date format! Please use YYYY-MM-DD format")
            return 0
        
        expenses_to_delete = []
        for exp_id, expense in self.expenses.items():
            exp_date_str = expense.get('date', '')
            try:
                exp_date = datetime.strptime(exp_date_str, "%Y-%m-%d")
                if exp_date == target_date:
                    expenses_to_delete.append(exp_id)
            except ValueError:
                continue
        
        if not expenses_to_delete:
            print(f"📭  No expenses found for date '{date}'")
            return 0
        
        print(f"⚠️  Are you sure you want to delete {len(expenses_to_delete)} expenses on date '{date}'?")
        confirmation = input("Type 'yes' to confirm: ").strip().lower()
        
        if confirmation == 'yes':
            deleted_count = 0
            for exp_id in expenses_to_delete:
                del self.expenses[exp_id]
                deleted_count += 1
            self.save_expenses()
            print(f"✅  Successfully deleted {deleted_count} expenses")
            return deleted_count
        else:
            print("❌  Deletion cancelled")
            return 0
    
    def delete_expenses_by_multiple_criteria(self, category=None, start_date=None, end_date=None, min_amount=None, max_amount=None):
        """
        Delete expenses matching multiple criteria
        Args:
            category: Category to match (optional)
            start_date: Start date (optional)
            end_date: End date (optional)
            min_amount: Minimum amount (optional)
            max_amount: Maximum amount (optional)
        Returns:
            int: Number of expenses deleted
        """
        if not self.expenses:
            print("⚠️  No expense records found!")
            return 0
        
        # First filter the expenses
        filtered_expenses = self.filter_expenses_by_multiple_criteria(category, start_date, end_date, min_amount, max_amount)
        
        if not filtered_expenses:
            print("No expenses to delete")
            return 0
        
        print(f"⚠️  Are you sure you want to delete {len(filtered_expenses)} expenses matching the criteria?")
        confirmation = input("Type 'yes' to confirm: ").strip().lower()
        
        if confirmation == 'yes':
            deleted_count = 0
            for exp_id in filtered_expenses.keys():
                del self.expenses[exp_id]
                deleted_count += 1
            self.save_expenses()
            print(f"✅  Successfully deleted {deleted_count} expenses")
            return deleted_count
        else:
            print("❌  Deletion cancelled")
            return 0
    
    def show_all_expenses(self):
        """Display all expenses"""
        if not self.expenses:
            print("📭  No expense records found!")
            return
        
        print("\n" + "="*60)
        print("📋 ALL EXPENSE RECORDS:")
        print("="*60)
        total = 0
        for exp_id, expense in self.expenses.items():
            self.display_single_expense(exp_id, expense)
            total += float(expense.get('amount', 0))
        print(f"💰 TOTAL: ${total:.2f}")
        print("="*60)

# Demo function for filtering and deleting
def filter_and_delete_demo():
    """Demonstration of filtering and deleting features"""
    tracker = ExpenseTracker()
    
    # Show all expenses
    tracker.show_all_expenses()
    
    # Example: Filter by category
    print("\n=== FILTER BY CATEGORY ===")
    category = input("Enter category to filter: ").strip()
    filtered = tracker.filter_expenses_by_category(category)
    tracker.display_filtered_expenses(filtered)
    
    # Example: Filter by date range
    print("\n=== FILTER BY DATE RANGE ===")
    start_date = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ").strip()
    end_date = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ").strip()
    filtered = tracker.filter_expenses_by_date_range(start_date or None, end_date or None)
    tracker.display_filtered_expenses(filtered)
    
    # Example: Filter by amount range
    print("\n=== FILTER BY AMOUNT RANGE ===")
    min_amount = input("Enter minimum amount or press Enter to skip: ").strip()
    max_amount = input("Enter maximum amount or press Enter to skip: ").strip()
    filtered = tracker.filter_expenses_by_amount_range(min_amount or None, max_amount or None)
    tracker.display_filtered_expenses(filtered)
    
    # Example: Filter by multiple criteria
    print("\n=== FILTER BY MULTIPLE CRITERIA ===")
    category = input("Enter category (or press Enter to skip): ").strip()
    start_date = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ").strip()
    end_date = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ").strip()
    min_amount = input("Enter minimum amount or press Enter to skip: ").strip()
    max_amount = input("Enter maximum amount or press Enter to skip: ").strip()
    
    filtered = tracker.filter_expenses_by_multiple_criteria(
        category if category else None,
        start_date if start_date else None,
        end_date if end_date else None,
        min_amount if min_amount else None,
        max_amount if max_amount else None
    )
    tracker.display_filtered_expenses(filtered)
    
    # Example: Delete single expense by ID
    print("\n=== DELETE SINGLE EXPENSE ===")
    expense_id = input("Enter expense ID to delete: ").strip()
    tracker.delete_expense_by_id(expense_id)
    
    # Example: Delete by category
    print("\n=== DELETE BY CATEGORY ===")
    category = input("Enter category to delete: ").strip()
    tracker.delete_expenses_by_category(category)
    
    # Example: Delete by date
    print("\n=== DELETE BY DATE ===")
    date = input("Enter date to delete (YYYY-MM-DD): ").strip()
    tracker.delete_expenses_by_date(date)
    
    # Show all expenses after deletions
    tracker.show_all_expenses()

if __name__ == "__main__":
    filter_and_delete_demo()
