function ToursViewModel()
{
    var self = this;
    self.tours = ko.observableArray([]);
    self.loadInfo = function () {
        $.ajax(
    {
        type: "GET",
        url: "../api/Customer/GetCustomerInfo",
        success: function (data) {
            self.tours(data);
            console.log(self.tours);
        },
        error: function (err) {
            console.log(err);
        }
    });
    };
    self.loadInfo();

    self.showPersonalInfo = function()
    {
        window.location.href = "#/personalInfo";
    }
}

ko.applyBindings(new ToursViewModel())