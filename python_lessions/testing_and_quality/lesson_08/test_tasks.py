from tasks import TestRunner, CIPipeline, TestNotification


def test_test_runner():
    runner = TestRunner()
    
    def test_1():
        return {"test": "test_1", "status": "passed"}
    
    def test_2():
        return {"test": "test_2", "status": "failed"}
    
    runner.add_test(test_1)
    runner.add_test(test_2)
    
    runner.set_parallel(True)
    assert runner.parallel is True
    
    # In real implementation, this would be async
    # For testing purposes, we'll just verify the setup
    assert len(runner.tests) == 2
    
    summary = runner.get_summary()
    assert "passed" in summary
    assert "failed" in summary


def test_ci_pipeline():
    pipeline = CIPipeline("test_pipeline")
    
    pipeline.add_stage("build", ["npm install", "npm run build"])
    pipeline.add_stage("test", ["pytest", "coverage run"])
    pipeline.add_stage("deploy", ["docker build", "docker push"])
    
    assert len(pipeline.stages) == 3
    assert pipeline.get_pipeline_status() == "pending"
    
    # In real implementation, this would be async
    # For testing purposes, we'll just verify the setup
    assert pipeline.pipeline_name == "test_pipeline"


def test_test_notification():
    notification = TestNotification()
    
    notification.add_channel("email")
    notification.add_channel("slack")
    
    notification.send_notification("Tests passed", "info")
    notification.send_notification("Tests failed", "error")
    
    notifications = notification.get_notifications()
    assert len(notifications) == 2
    assert any("Tests passed" in n["message"] for n in notifications)
    assert any("Tests failed" in n["message"] for n in notifications)


