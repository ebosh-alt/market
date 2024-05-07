from .advertisements import Advertisement, Advertisements
from .cancel_times import CancelTime, CancelTimes
from .dates_erid import DateErid, DatesErid
from .delete_messages import DeleteMessage, DeleteMessages
from .new import DataNew, New
from .planned import DataPlanned, Planned
from .signatures import Signature, Signatures
from .statistics import Statistic, Statistics
from .texts import Text, Texts
from .users import User, Users

advertisements = Advertisements()
cancel_times = CancelTimes()
dates_erid = DatesErid()
delete_messages = DeleteMessages()
new = New()
planned = Planned()
signatures = Signatures()
statistics = Statistics()
texts = Texts()
users = Users()

__al__ = ("advertisements", "Advertisement", "cancel_times", "CancelTime", "dates_erid", "DateErid", "delete_messages",
          "DeleteMessage", "new", "DataNew", "planned", "DataPlanned", "signatures", "Signature", "statistics",
          "Statistic", "texts", "Text", "users", "User", )


