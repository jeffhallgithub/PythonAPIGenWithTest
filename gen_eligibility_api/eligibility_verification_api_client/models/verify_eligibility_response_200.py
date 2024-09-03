from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyEligibilityResponse200")


@_attrs_define
class VerifyEligibilityResponse200:
    """
    Attributes:
        eligible (Union[Unset, bool]): Indicates if the patient is eligible (true) or not (false)
        message (Union[Unset, str]): Additional information or reason if the patient is not eligible
    """

    eligible: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eligible = self.eligible

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eligible = d.pop("eligible", UNSET)

        message = d.pop("message", UNSET)

        verify_eligibility_response_200 = cls(
            eligible=eligible,
            message=message,
        )

        verify_eligibility_response_200.additional_properties = d
        return verify_eligibility_response_200

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
