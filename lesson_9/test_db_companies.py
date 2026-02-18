import pytest
from company_table import CompanyTable

db_connection_string  = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

db = CompanyTable(db_connection_string )


def test_db_connection():
    tables = db.get_table_names()
    assert 'company' in tables


def test_get_companies():

    companies = db.get_companies()
    assert isinstance(companies, list)


def test_get_active_companies():

    all_companies = db.get_companies()
    active_companies = db.get_active_companies()

    assert len(active_companies) <= len(all_companies)

    if active_companies:
        for company in active_companies:
            assert company['is_active'] is True


def test_create_and_verify_company():

    companies_before = db.get_companies()
    count_before = len(companies_before)

    new_name = "SQLAlchemy Test Company"
    new_description = "Created by automated test"

    db.create_company(new_name, new_description)

    companies_after = db.get_companies()
    count_after = len(companies_after)

    assert count_after - count_before == 1

    new_company_id = db.get_max_id()

    new_company_data = db.get_company_by_id(new_company_id)

    assert len(new_company_data) == 1

    created_company = new_company_data[0]
    assert created_company['name'] == new_name
    assert created_company['description'] == new_description
    assert created_company['is_active'] is True

    db.delete_company_by_id(new_company_id)


def test_get_company_by_id():

    name = "Company for ID test"
    description = "Temporary company"
    db.create_company(name, description)
    created_id = db.get_max_id()

    company_list = db.get_company_by_id(created_id)

    assert len(company_list) == 1
    found_company = company_list[0]

    assert found_company['id'] == created_id
    assert found_company['name'] == name
    assert found_company['description'] == description
    assert found_company['is_active'] is True

    db.delete_company_by_id(created_id)


def test_get_inactive_company_by_id():

    name = "Company to delete"
    db.create_company(name, "")
    created_id = db.get_max_id()

    db.delete_company_by_id(created_id)

    company_after_delete = db.get_company_by_id(created_id)

    assert len(company_after_delete) == 0


def test_loop_over_companies():
    all_companies = db.get_companies()

    new_name = "Company for loop test"
    db.create_company(new_name, "")
    new_id = db.get_max_id()

    all_companies_updated = db.get_companies()

    found = False
    for company in all_companies_updated:
        if company['id'] == new_id:
            found = True
            assert company['name'] == new_name

    assert found

    db.delete_company_by_id(new_id)
