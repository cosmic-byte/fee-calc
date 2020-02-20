from fee_calculator.apps.core import constants


class LoanApplication:
    def __init__(self, tenure: int, loan_amount: float):
        self.tenure = tenure
        self.loan_amount = loan_amount
        self.loan_fee = 0


class FeeCalculator:
    def __init__(self, application: LoanApplication):
        self._loan_amount = application.loan_amount
        self._tenure = application.tenure

    def calculate(self):
        """
        Calculate loan fee for a given loan application which includes the loan tenure and amount.

        Returns:
        loan_fee (float): Loan fee.

        """
        low_bound, high_bound = self._get_loan_boundaries()
        if low_bound == high_bound:
            return constants.FEE_STRUCTURE[self._tenure][low_bound]

        low_bound_fee = constants.FEE_STRUCTURE[self._tenure][low_bound]
        high_bound_fee = constants.FEE_STRUCTURE[self._tenure][high_bound]

        # Linear interpolation. Check https://en.wikipedia.org/wiki/Linear_interpolation for more details.
        loan_fee = (
            ((self._loan_amount - low_bound) * (high_bound_fee - low_bound_fee))
            / (high_bound - low_bound)
        ) + low_bound_fee
        return self._round_loan_fee(loan_fee)

    def _get_loan_boundaries(self):
        """
        Get fixed lower and upper loan amount boundaries for a given loan amount.

        Returns:
        boundaries (tuple): Tuple of lower and upper bound.

        """
        fee_structure = constants.FEE_STRUCTURE[self._tenure]
        low_bound = 0
        high_bound = 0

        # considering the structure is small (20), we can loop through to find the bounds
        for amount in fee_structure.keys():
            if self._loan_amount == float(amount):
                low_bound = amount
                high_bound = amount
                break
            elif self._loan_amount > float(amount):
                low_bound = amount
            else:
                high_bound = amount

            if low_bound != 0 and high_bound != 0:
                break
        return low_bound, high_bound

    def _round_loan_fee(self, loan_fee):
        """
        Round loan fee such that (loan fee + loan amount) is an exact multiple of the set multiplier (5).
        Eg: if loan_fee = 4 and loan_amount = 50.4,
            rounded loan_fee should be 4.6
            ie 4.6 + 50.4 = 55 (which is now an exact multiple of 5)

        Parameters:
        loan_fee (float): Loan fee to round.

        Returns:
        loan_fee (float): A rounded loan fee.

        """
        multiplier = constants.BASE_FEE_MULTIPLIER
        fixed_amount = self._loan_amount + loan_fee
        rounded_fixed_amount = multiplier * round(fixed_amount / multiplier)
        difference = rounded_fixed_amount - fixed_amount
        return round(loan_fee + difference, 2)

    def __setattr__(self, key, value):
        """
        Ensure that loan amount and tenure can only be set via the constructor.
        """
        if key in self.__dict__ and key.startswith("_"):
            raise AttributeError("You can't modify a private attribute")
        self.__dict__[key] = value
