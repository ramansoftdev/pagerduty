import pytest

from  pagerduty.pagerduty import PagerDuty 


# To test candidate setup, expect test to run with failure
def test_dispatch_alert__implemented():
    pagerduty = PagerDuty()

    try:
        pagerduty.add_person(1)
        pagerduty.add_person(2)
        pagerduty.add_person(3)

        assert len(pagerduty.engineer_pool) == 2

        pagerduty.dispatch_alert()

        assert len(pagerduty.engineer_pool) == 1

        pagerduty.dispatch_alert()
        assert len(pagerduty.manager_pool) == 1
        assert len(pagerduty.engineer_pool) == 0

        pagerduty.dispatch_alert()
        assert len(pagerduty.manager_pool) == 0 
        assert len(pagerduty.engineer_pool) == 0

        with pytest.raises(KeyError)  as failinfo:
            pagerduty.dispatch_alert()
            assert len(pagerduty.manager_pool) == 0
            assert len(pagerduty.engineer_pool) == 0

        
    except NotImplementedError:
        pytest.fail("dispatch_alert() raised NotImplementedError!")

