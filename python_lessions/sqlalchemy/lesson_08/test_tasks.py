from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tasks import DatabaseTestSuite, DataIntegrityChecker, PerformanceTester


def test_database_test_suite():
    suite = DatabaseTestSuite("sqlite:///:memory:")
    suite.setup()
    
    # Test connection
    is_connected = suite.test_connection()
    assert is_connected is True
    
    # Test queries
    query_results = suite.test_queries()
    assert isinstance(query_results, list)
    
    # Run all tests
    results = suite.run_tests()
    assert isinstance(results, list)
    
    suite.teardown()


def test_data_integrity_checker():
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    checker = DataIntegrityChecker(session)
    
    # Test foreign key checks
    fk_checks = checker.check_foreign_keys()
    assert isinstance(fk_checks, list)
    
    # Test unique constraint checks
    unique_checks = checker.check_unique_constraints()
    assert isinstance(unique_checks, list)
    
    # Test data type checks
    type_checks = checker.check_data_types()
    assert isinstance(type_checks, list)
    
    # Run all checks
    all_checks = checker.run_all_checks()
    assert isinstance(all_checks, dict)
    
    session.close()


def test_performance_tester():
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    tester = PerformanceTester(session)
    
    # Test query performance
    query_perf = tester.test_query_performance("SELECT 1", 10)
    assert "execution_time" in query_perf
    assert "iterations" in query_perf
    
    # Test insert performance
    insert_data = [{"name": f"test_{i}"} for i in range(10)]
    insert_perf = tester.test_insert_performance(insert_data)
    assert "execution_time" in insert_perf
    
    # Test update performance
    update_data = [{"id": i, "name": f"updated_{i}"} for i in range(10)]
    update_perf = tester.test_update_performance(update_data)
    assert "execution_time" in update_perf
    
    # Get performance summary
    summary = tester.get_performance_summary()
    assert isinstance(summary, dict)
    
    session.close()


