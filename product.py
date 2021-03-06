from currency import Currency


class Product:
    def __init__(self, name, store, product_type, url, key, stock,
                 normal_price, offer_price, currency, part_number=None,
                 sku=None, description=None, cell_plan_name=None,
                 cell_monthly_payment=None):
        self.name = name
        self.store = store
        self.product_type = product_type
        self.url = url
        self.key = key
        self.stock = stock
        self.normal_price = normal_price
        self.offer_price = offer_price
        self.currency = currency
        self.part_number = part_number
        self.sku = sku
        self.description = description
        self.cell_plan_name = cell_plan_name
        self.cell_monthly_payment = cell_monthly_payment

    def __str__(self):
        lines = list()
        lines.append('{} - {} ({})'.format(self.store, self.name,
                                           self.product_type))
        lines.append(self.url)
        lines.append('SKU: {}'.format(
            self._optional_field_as_string('sku')))
        lines.append('Part number: {}'.format(
            self._optional_field_as_string('part_number')))
        lines.append(u'Key: {}'.format(self.key))
        lines.append(u'Stock: {}'.format(self._stock_as_string()))
        lines.append(u'Currency: {}'.format(self.currency))
        lines.append(u'Normal price: {}'.format(Currency.format(
            self.normal_price, self.currency)))
        lines.append(u'Offer price: {}'.format(Currency.format(
            self.offer_price, self.currency)))
        lines.append('Cell plan name: {}'.format(
            self._optional_field_as_string('cell_plan_name')))

        cell_monthly_payment = self.cell_monthly_payment

        if cell_monthly_payment is None:
            cell_monthly_payment_string = 'N/A'
        else:
            cell_monthly_payment_string = Currency.format(
                cell_monthly_payment, self.currency)

        lines.append('Cell monthly payment: {}'.format(
            cell_monthly_payment_string))

        lines.append('Description: {}'.format(
            self._optional_field_as_string('description')[:30]))

        return '\n'.join(lines)

    def serialize(self):
        return {
            'name': self.name,
            'store': self.store,
            'product_type': self.product_type,
            'url': self.url,
            'key': self.key,
            'stock': self.stock,
            'normal_price': self.normal_price,
            'offer_price': self.offer_price,
            'currency': self.currency,
            'part_number': self.part_number,
            'sku': self.sku,
            'description': self.description,
            'cell_plan_name': self.cell_plan_name,
            'cell_monthly_payment': self.cell_monthly_payment
        }

    def _stock_as_string(self):
        if self.stock == -1:
            return 'Available but unknown'
        elif self.stock == 0:
            return 'Unavailable'
        else:
            return str(self.stock)

    def _optional_field_as_string(self, field):
        field_value = getattr(self, field)
        if field_value is not None:
            return field_value
        else:
            return 'N/A'
