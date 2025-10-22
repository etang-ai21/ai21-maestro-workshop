from fastmcp import FastMCP
from typing import Dict, Optional

# Initialize FastMCP server
mcp = FastMCP("Employee Knowledge Base")

# Sample employee data (in production, this would come from a database)
EMPLOYEE_DATA = {
    "EMP001": {
        "name": "Alice Johnson",
        "department": "Engineering",
        "role": "Senior Developer",
        "salary": 120000,
        "email": "alice.johnson@company.com",
        "manager": "EMP005"
    },
    "EMP002": {
        "name": "Bob Smith",
        "department": "Sales",
        "role": "Sales Manager",
        "salary": 95000,
        "email": "bob.smith@company.com",
        "manager": "EMP006"
    },
    "EMP003": {
        "name": "Carol White",
        "department": "HR",
        "role": "HR Specialist",
        "salary": 75000,
        "email": "carol.white@company.com",
        "manager": "EMP007"
    },
    "EMP004": {
        "name": "David Brown",
        "department": "Engineering",
        "role": "Junior Developer",
        "salary": 80000,
        "email": "david.brown@company.com",
        "manager": "EMP005"
    },
    "EMP005": {
        "name": "Eva Martinez",
        "department": "Engineering",
        "role": "Engineering Manager",
        "salary": 150000,
        "email": "eva.martinez@company.com",
        "manager": "EMP008"
    }
}

@mcp.tool()
def get_employee_by_id(employee_id: str) -> Dict:
    """
    Retrieve employee information by their ID.
    
    Args:
        employee_id: The unique employee identifier (e.g., EMP001)
    
    Returns:
        Employee information including name, department, role, and salary
    """
    if employee_id in EMPLOYEE_DATA:
        return {
            "success": True,
            "data": EMPLOYEE_DATA[employee_id]
        }
    else:
        return {
            "success": False,
            "error": f"Employee with ID {employee_id} not found"
        }
        
@mcp.tool()
def search_employee_by_name(name_query: str, max_results: Optional[int] = 10) -> Dict:
    """
    Search for employees by name using fuzzy matching.
    
    Args:
        name_query: The name or partial name to search for
        max_results: Maximum number of results to return (default: 10)
    
    Returns:
        List of employees matching the name query, sorted by relevance
    """
    if not name_query.strip():
        return {
            "success": False,
            "error": "Name query cannot be empty"
        }
    
    query = name_query.lower().strip()
    matches = []
    
    for emp_id, emp_data in EMPLOYEE_DATA.items():
        employee_name = emp_data["name"].lower()
        score = 0
        
        # Exact match gets highest score
        if query == employee_name:
            score = 100
        # Check if query is contained in name
        elif query in employee_name:
            score = 80
        # Check if all words in query are in name
        elif all(word in employee_name for word in query.split()):
            score = 60
        # Check if any word in query matches any word in name
        elif any(word in employee_name for word in query.split()):
            score = 40
        # Check if name starts with query
        elif employee_name.startswith(query):
            score = 70
        # Check for partial word matches
        else:
            query_words = query.split()
            name_words = employee_name.split()
            partial_matches = 0
            for q_word in query_words:
                for n_word in name_words:
                    if q_word in n_word or n_word in q_word:
                        partial_matches += 1
                        break
            if partial_matches > 0:
                score = 20 + (partial_matches * 10)
        
        if score > 0:
            matches.append({
                "id": emp_id,
                "score": score
            })
    
    # Sort by score (highest first)
    matches.sort(key=lambda x: x["score"], reverse=True)
    
    # Limit results
    if max_results:
        matches = matches[:max_results]
    
    return {
        "success": True,
        "query": name_query,
        "count": len(matches),
        "employee_ids": [match["id"] for match in matches]
    }


@mcp.tool()
def search_employees_by_department(department: str) -> Dict:
    """
    Search for all employees in a specific department.
    
    Args:
        department: The department name to search for
    
    Returns:
        List of employees in the specified department
    """
    employees = []
    for emp_id, emp_data in EMPLOYEE_DATA.items():
        if emp_data["department"].lower() == department.lower():
            employees.append({
                "id": emp_id,
                **emp_data
            })
    
    return {
        "success": True,
        "count": len(employees),
        "employees": employees
    }

@mcp.tool()
def get_salary_range(min_salary: Optional[int] = None, max_salary: Optional[int] = None) -> Dict:
    """
    Find employees within a specific salary range.
    
    Args:
        min_salary: Minimum salary threshold (optional)
        max_salary: Maximum salary threshold (optional)
    
    Returns:
        List of employees within the specified salary range
    """
    employees = []
    for emp_id, emp_data in EMPLOYEE_DATA.items():
        salary = emp_data["salary"]
        if (min_salary is None or salary >= min_salary) and \
           (max_salary is None or salary <= max_salary):
            employees.append({
                "id": emp_id,
                "name": emp_data["name"],
                "department": emp_data["department"],
                "salary": salary
            })
    
    # Sort by salary
    employees.sort(key=lambda x: x["salary"], reverse=True)
    
    return {
        "success": True,
        "count": len(employees),
        "employees": employees
    }

@mcp.tool()
def get_employee_hierarchy(employee_id: str) -> Dict:
    """
    Get the reporting hierarchy for an employee.
    
    Args:
        employee_id: The employee ID to get hierarchy for
    
    Returns:
        The employee's manager and any direct reports
    """
    if employee_id not in EMPLOYEE_DATA:
        return {
            "success": False,
            "error": f"Employee with ID {employee_id} not found"
        }
    
    employee = EMPLOYEE_DATA[employee_id]
    
    # Find manager
    manager = None
    if employee.get("manager") and employee["manager"] in EMPLOYEE_DATA:
        manager = {
            "id": employee["manager"],
            "name": EMPLOYEE_DATA[employee["manager"]]["name"],
            "role": EMPLOYEE_DATA[employee["manager"]]["role"]
        }
    
    # Find direct reports
    direct_reports = []
    for emp_id, emp_data in EMPLOYEE_DATA.items():
        if emp_data.get("manager") == employee_id:
            direct_reports.append({
                "id": emp_id,
                "name": emp_data["name"],
                "role": emp_data["role"]
            })
    
    return {
        "success": True,
        "employee": {
            "id": employee_id,
            "name": employee["name"],
            "role": employee["role"]
        },
        "manager": manager,
        "direct_reports": direct_reports
    }

@mcp.tool()
def get_department_statistics() -> Dict:
    """
    Get statistics for all departments including employee count and average salary.
    
    Returns:
        Statistics for each department
    """
    dept_stats = {}
    
    for emp_data in EMPLOYEE_DATA.values():
        dept = emp_data["department"]
        if dept not in dept_stats:
            dept_stats[dept] = {
                "count": 0,
                "total_salary": 0,
                "employees": []
            }
        
        dept_stats[dept]["count"] += 1
        dept_stats[dept]["total_salary"] += emp_data["salary"]
        dept_stats[dept]["employees"].append(emp_data["name"])
    
    # Calculate averages
    result = {}
    for dept, stats in dept_stats.items():
        result[dept] = {
            "employee_count": stats["count"],
            "average_salary": stats["total_salary"] / stats["count"],
            "total_salary": stats["total_salary"],
            "employees": stats["employees"]
        }
    
    return {
        "success": True,
        "departments": result
    }

async def run_server():
    await mcp.run_async(transport="streamable-http", path="/mcp", port=8000)
    
# Run the server
if __name__ == "__main__":
    import asyncio
    asyncio.run(run_server())