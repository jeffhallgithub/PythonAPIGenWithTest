import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="VerifyEligibilityBody")


@_attrs_define
class VerifyEligibilityBody:
    """
    Attributes:
        carrier_name (str):
        member_id (str):
        full_name (str):
        dob (datetime.date):
    """

    carrier_name: str
    member_id: str
    full_name: str
    dob: datetime.date
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_name = self.carrier_name

        member_id = self.member_id

        full_name = self.full_name

        dob = self.dob.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "carrier_name": carrier_name,
                "member_id": member_id,
                "full_name": full_name,
                "dob": dob,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carrier_name = d.pop("carrier_name")

        member_id = d.pop("member_id")

        full_name = d.pop("full_name")

        dob = isoparse(d.pop("dob")).date()

        verify_eligibility_body = cls(
            carrier_name=carrier_name,
            member_id=member_id,
            full_name=full_name,
            dob=dob,
        )

        verify_eligibility_body.additional_properties = d
        return verify_eligibility_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
