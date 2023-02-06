from odoo import fields, models


class empresa(models.Model):
    _name = "gestionfcts.empresa"
    _description = "Descripción"

    name = fields.Char("Nombre", required=True)
    contact = fields.Char("Persona de contacto")
    telephone = fields.Integer("Teléfono de contacto")
    direccion = fields.Char("Dirección")
    localidad = fields.Char("Localidad")
    fp = fields.Selection([('0', 'Si'), ('1', 'No')], "FP", default='0')
    erasmus = fields.Selection([('0', 'Si'), ('1', 'No')], "Erasmus", default='0')
    plazas = fields.Char("Plazas a ofertar")
    convenio = fields.Selection([('0', 'Si'), ('1', 'No')], "Convenio", default='0')
    tareas = fields.Char("Tareas a realizar")
    observaciones = fields.Char("Observaciones")

    alumno_id = fields.One2many("gestionfcts.alumno", "empresa_id", "Alumnos")
