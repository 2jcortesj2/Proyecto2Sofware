-- ============================================
-- Script de Base de Datos de Ejemplo
-- Sistema BioLab LIS - clinical_data
-- ============================================

-- Usar la base de datos
USE clinical_data;

-- ============================================
-- TABLA: paciente
-- ============================================

-- Limpiar datos existentes (opcional)
-- DELETE FROM resultado_perfil_lipidico;
-- DELETE FROM laboratorista;
-- DELETE FROM paciente;

-- TABLA paciente
CREATE TABLE paciente (
    paciente_id VARCHAR(10) NOT NULL,          -- p.ej. 'P001'
    codigo_ingreso VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(30),
    insurance VARCHAR(100),
    fecha_registro DATE,
    PRIMARY KEY (paciente_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- TABLA laboratorista
CREATE TABLE laboratorista (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,   -- id numérico para FK en resultados
    codigo_interno VARCHAR(20) NOT NULL,       -- p.ej. 'LAB001'
    nombre VARCHAR(150) NOT NULL,
    titulo VARCHAR(80),
    telefono VARCHAR(30),
    email VARCHAR(150),
    especialidad VARCHAR(120),
    PRIMARY KEY (id),
    UNIQUE KEY ux_laboratorista_codigo (codigo_interno),
    UNIQUE KEY ux_laboratorista_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- TABLA resultado_perfil_lipidico
CREATE TABLE resultado_perfil_lipidico (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    paciente_id VARCHAR(10) NOT NULL,
    laboratorista_id INT UNSIGNED NOT NULL,
    colesterol_total DECIMAL(6,2),   -- ej: 225.00
    colesterol_hdl DECIMAL(6,2),
    colesterol_ldl DECIMAL(6,2),
    trigliceridos DECIMAL(6,2),
    fecha_analisis DATE,
    observaciones TEXT,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_rpl_paciente (paciente_id),
    KEY idx_rpl_laboratorista (laboratorista_id),
    CONSTRAINT fk_rpl_paciente FOREIGN KEY (paciente_id)
        REFERENCES paciente (paciente_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_rpl_laboratorista FOREIGN KEY (laboratorista_id)
        REFERENCES laboratorista (id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insertar pacientes de ejemplo
INSERT INTO paciente (paciente_id, codigo_ingreso, nombre, apellidos, direccion, telefono, insurance, fecha_registro) VALUES
('P001', 'ING-00156', 'María', 'García López', 'Calle 10 #45-67, Medellín', '3001234567', 'Sura EPS', '2024-10-15'),
('P002', 'ING-00157', 'Carlos', 'Rodríguez Pérez', 'Carrera 80 #32-15, Medellín', '3107654321', 'Nueva EPS', '2024-10-16'),
('P003', 'ING-00158', 'Ana', 'Martínez Silva', 'Calle 50 #70-25, Medellín', '3209876543', 'Sanitas EPS', '2024-10-17'),
('P004', 'ING-00159', 'Luis', 'Hernández Castro', 'Carrera 43A #12-34, Medellín', '3151234567', 'Salud Total', '2024-10-18'),
('P005', 'ING-00160', 'Patricia', 'González Ramírez', 'Calle 33 #55-88, Medellín', '3187654321', 'Sura EPS', '2024-10-19'),
('P006', 'ING-00161', 'Jorge', 'López Morales', 'Carrera 65 #48-90, Medellín', '3229876543', 'Coomeva EPS', '2024-10-20'),
('P007', 'ING-00162', 'Sandra', 'Díaz Torres', 'Calle 20 #30-45, Medellín', '3001112233', 'Nueva EPS', '2024-10-21'),
('P008', 'ING-00163', 'Roberto', 'Vargas Jiménez', 'Carrera 70 #25-60, Medellín', '3104445566', 'Sanitas EPS', '2024-10-22'),
('P009', 'ING-00164', 'Laura', 'Castillo Reyes', 'Calle 45 #82-15, Medellín', '3207778899', 'Salud Total', '2024-10-23'),
('P010', 'ING-00165', 'Miguel', 'Ruiz Fernández', 'Carrera 52 #18-77, Medellín', '3150001122', 'Sura EPS', '2024-10-24');

-- ============================================
-- TABLA: laboratorista
-- ============================================

INSERT INTO laboratorista (codigo_interno, nombre, titulo, telefono, email, especialidad) VALUES
('LAB001', 'Dra. Ana López Méndez', 'Bacterióloga', '3001234567', 'ana.lopez@biolab.com', 'Química Clínica'),
('LAB002', 'Dr. Luis Martínez Soto', 'Microbiólogo', '3107654321', 'luis.martinez@biolab.com', 'Microbiología Clínica'),
('LAB003', 'Dra. Carmen Silva Ortiz', 'Bióloga', '3209876543', 'carmen.silva@biolab.com', 'Hematología'),
('LAB004', 'Dr. Pedro Ramírez Vega', 'Bacteriólogo', '3151234567', 'pedro.ramirez@biolab.com', 'Bioquímica'),
('LAB005', 'Dra. Sofia Torres Muñoz', 'Química', '3187654321', 'sofia.torres@biolab.com', 'Química Clínica');

-- ============================================
-- TABLA: resultado_perfil_lipidico
-- ============================================

-- Resultados con valores normales
INSERT INTO resultado_perfil_lipidico (paciente_id, laboratorista_id, colesterol_total, colesterol_hdl, colesterol_ldl, trigliceridos, fecha_analisis, observaciones) VALUES
('P001', 1, 185.5, 52.0, 115.0, 130.0, '2024-10-24', 'Valores dentro del rango normal. Paciente mantiene dieta balanceada y ejercicio regular.'),
('P003', 2, 178.0, 58.0, 105.0, 125.0, '2024-10-25', 'Perfil lipídico excelente. Continuar con estilo de vida saludable.'),
('P005', 3, 192.0, 55.0, 118.0, 135.0, '2024-10-26', 'Valores normales. Se recomienda control anual.');

-- Resultados con colesterol total elevado
INSERT INTO resultado_perfil_lipidico (paciente_id, laboratorista_id, colesterol_total, colesterol_hdl, colesterol_ldl, trigliceridos, fecha_analisis, observaciones) VALUES
('P002', 1, 225.0, 45.0, 145.0, 175.0, '2024-10-25', 'Colesterol total elevado. Se recomienda modificación en la dieta y aumento de actividad física. Control en 3 meses.'),
('P004', 2, 238.0, 42.0, 158.0, 190.0, '2024-10-26', 'Hipercolesterolemia leve. Reducir consumo de grasas saturadas. Valoración por nutrición.');

-- Resultados con LDL elevado
INSERT INTO resultado_perfil_lipidico (paciente_id, laboratorista_id, colesterol_total, colesterol_hdl, colesterol_ldl, trigliceridos, fecha_analisis, observaciones) VALUES
('P006', 4, 205.0, 48.0, 132.0, 145.0, '2024-10-27', 'LDL limítrofe alto. Reducir consumo de alimentos procesados. Control en 6 meses.'),
('P008', 5, 218.0, 50.0, 140.0, 155.0, '2024-10-28', 'Colesterol LDL elevado. Iniciar programa de ejercicio cardiovascular.');

-- Resultados con triglicéridos elevados
INSERT INTO resultado_perfil_lipidico (paciente_id, laboratorista_id, colesterol_total, colesterol_hdl, colesterol_ldl, trigliceridos, fecha_analisis, observaciones) VALUES
('P007', 1, 210.0, 46.0, 125.0, 195.0, '2024-10-27', 'Triglicéridos elevados. Reducir consumo de azúcares y carbohidratos refinados. Evitar alcohol.'),
('P009', 3, 198.0, 51.0, 120.0, 165.0, '2024-10-29', 'Triglicéridos limítrofe alto. Aumentar consumo de omega-3 y fibra.');

-- Resultado con HDL bajo
INSERT INTO resultado_perfil_lipidico (paciente_id, laboratorista_id, colesterol_total, colesterol_hdl, colesterol_ldl, trigliceridos, fecha_analisis, observaciones) VALUES
('P010', 4, 188.0, 38.0, 112.0, 140.0, '2024-10-30', 'HDL bajo (colesterol bueno). Aumentar actividad física aeróbica. Considerar incluir nueces y aceite de oliva en la dieta.');

-- ============================================
-- CONSULTAS DE VERIFICACIÓN
-- ============================================

-- Verificar datos insertados
SELECT 'Pacientes registrados:' as Info, COUNT(*) as Total FROM paciente;
SELECT 'Laboratoristas registrados:' as Info, COUNT(*) as Total FROM laboratorista;
SELECT 'Resultados registrados:' as Info, COUNT(*) as Total FROM resultado_perfil_lipidico;

-- Ver todos los pacientes
SELECT * FROM paciente;

-- Ver todos los laboratoristas
SELECT * FROM laboratorista;

-- Ver todos los resultados con información completa
SELECT 
    r.id,
    r.paciente_id,
    CONCAT(p.nombre, ' ', p.apellidos) as paciente_nombre,
    CONCAT(l.nombre) as laboratorista,
    r.colesterol_total,
    r.colesterol_hdl,
    r.colesterol_ldl,
    r.trigliceridos,
    r.fecha_analisis,
    r.observaciones
FROM resultado_perfil_lipidico r
INNER JOIN paciente p ON r.paciente_id = p.paciente_id
INNER JOIN laboratorista l ON r.laboratorista_id = l.id
ORDER BY r.fecha_analisis DESC;

-- ============================================
-- SCRIPT COMPLETADO
-- ============================================