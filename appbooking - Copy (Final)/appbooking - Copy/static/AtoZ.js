// conditions.js - Handles the A-Z disease/condition display functionality

// Data structure containing diseases and body parts for each letter
const medicalData = {
  'A': {
    diseases: ['Allergies', 'Asthma', 'Arthritis', 'Anemia', 'Appendicitis'],
    bodyParts: ['Arm', 'Abdomen', 'Ankle', 'Aorta']
  },
  'B': {
    diseases: ['Bronchitis', 'Bursitis', 'Bipolar Disorder', 'Bell\'s Palsy'],
    bodyParts: ['Back', 'Brain', 'Breast', 'Bladder']
  },
  'C': {
    diseases: ['Cardiovascular Disease', 'Chickenpox', 'Cholera', 'Cataracts', 'Cancer'],
    bodyParts: ['Chest', 'Cervix', 'Clavicle', 'Coccyx']
  },
  'D': {
    diseases: ['Diabetes', 'Depression', 'Dementia', 'Dengue'],
    bodyParts: ['Diaphragm', 'Duodenum', 'Dermis']
  },
  'E': {
    diseases: ['Eczema', 'Epilepsy', 'Emphysema', 'Endometriosis'],
    bodyParts: ['Ear', 'Elbow', 'Esophagus', 'Epidermis']
  },
  'F': {
    diseases: ['Fibromyalgia', 'Flu', 'Food Poisoning', 'Fracture'],
    bodyParts: ['Foot', 'Forearm', 'Femur', 'Face']
  },
  'G': {
    diseases: ['Gastritis', 'Gout', 'Glaucoma', 'Gingivitis'],
    bodyParts: ['Groin', 'Gallbladder', 'Gums', 'Gluteus']
  },
  'H': {
    diseases: ['Hypertension', 'Hepatitis', 'Hemorrhoids', 'HIV/AIDS'],
    bodyParts: ['Hand', 'Heart', 'Hip', 'Humerus']
  },
  'I': {
    diseases: ['Influenza', 'Insomnia', 'IBS', 'Impetigo'],
    bodyParts: ['Intestine', 'Iris', 'Incisor']
  },
  'J': {
    diseases: ['Jaundice', 'Joint Pain', 'Juvenile Arthritis'],
    bodyParts: ['Jaw', 'Jejunum', 'Joints']
  },
  'K': {
    diseases: ['Kidney Stones', 'Kawasaki Disease', 'Keratitis'],
    bodyParts: ['Kidney', 'Knee', 'Knuckle']
  },
  'L': {
    diseases: ['Laryngitis', 'Lupus', 'Leukemia', 'Lyme Disease'],
    bodyParts: ['Liver', 'Lung', 'Larynx', 'Leg']
  },
  'M': {
    diseases: ['Malaria', 'Migraine', 'Meningitis', 'Measles'],
    bodyParts: ['Mouth', 'Muscle', 'Mandible', 'Metacarpals']
  },
  'N': {
    diseases: ['Narcolepsy', 'Norovirus', 'Neuropathy', 'Nephritis'],
    bodyParts: ['Nose', 'Neck', 'Nerves', 'Nails']
  },
  'O': {
    diseases: ['Osteoporosis', 'Obesity', 'Osteoarthritis', 'Otitis'],
    bodyParts: ['Ovary', 'Occipital Bone', 'Oesophagus']
  },
  'P': {
    diseases: ['Pneumonia', 'Psoriasis', 'Parkinson\'s', 'Polio'],
    bodyParts: ['Pancreas', 'Pelvis', 'Phalanges', 'Prostate']
  },
  'Q': {
    diseases: ['Q Fever'],
    bodyParts: ['Quadriceps']
  },
  'R': {
    diseases: ['Rabies', 'Rheumatism', 'Rubella', 'Rosacea'],
    bodyParts: ['Ribs', 'Retina', 'Radius', 'Rectum']
  },
  'S': {
    diseases: ['Sinusitis', 'Stroke', 'Scoliosis', 'Sepsis'],
    bodyParts: ['Stomach', 'Spine', 'Spleen', 'Skin']
  },
  'T': {
    diseases: ['Tuberculosis', 'Tonsillitis', 'Tetanus', 'Thyroid Disorders'],
    bodyParts: ['Teeth', 'Tongue', 'Tibia', 'Trachea']
  },
  'U': {
    diseases: ['Ulcer', 'Uveitis', 'Urinary Tract Infection'],
    bodyParts: ['Uterus', 'Uvula', 'Ulnar']
  },
  'V': {
    diseases: ['Varicose Veins', 'Vertigo', 'Vitiligo'],
    bodyParts: ['Vertebrae', 'Vulva', 'Ventricle']
  },
  'W': {
    diseases: ['Whooping Cough', 'West Nile Virus'],
    bodyParts: ['Wrist', 'White Blood Cells']
  },
  'X': {
    diseases: ['Xeroderma Pigmentosum', 'Xerophthalmia'],
    bodyParts: ['Xiphoid Process']
  },
  'Y': {
    diseases: ['Yellow Fever'],
    bodyParts: ['Yolk Sac (embryonic)']
  },
  'Z': {
    diseases: ['Zika Virus', 'Zollinger-Ellison Syndrome'],
    bodyParts: ['Zygomatic Bone']
  },
  '#': {
    diseases: ['5-alpha-reductase deficiency', '1p36 deletion syndrome'],
    bodyParts: ['7th cervical vertebra']
  }
};

// Function to create and display the results container
function createResultsContainer() {
  const resultsContainer = document.createElement('div');
  resultsContainer.id = 'medical-results';
  resultsContainer.style.marginTop = '2rem';
  resultsContainer.style.padding = '1.5rem';
  resultsContainer.style.backgroundColor = '#f8f9fa';
  resultsContainer.style.borderRadius = '8px';
  resultsContainer.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
  
  const conditionsWrapper = document.querySelector('.conditions-wrapper');
  conditionsWrapper.appendChild(resultsContainer);
  
  return resultsContainer;
}

// Function to display medical information for a selected letter
function displayMedicalInfo(letter) {
  let resultsContainer = document.getElementById('medical-results');
  
  // Create the container if it doesn't exist
  if (!resultsContainer) {
    resultsContainer = createResultsContainer();
  }
  
  const data = medicalData[letter];
  
  if (data) {
    // Create HTML content
    let html = `<h3 style="color: #0047ab; margin-bottom: 1rem;">Results for "${letter}"</h3>`;
    
    // Diseases section
    html += `<div style="margin-bottom: 1.5rem;">`;
    html += `<h4 style="color: #1E40AF; margin-bottom: 0.5rem;">Diseases/Conditions</h4>`;
    html += `<ul style="columns: 2; column-gap: 2rem; list-style-type: disc; padding-left: 1.5rem;">`;
    data.diseases.forEach(disease => {
      html += `<li style="margin-bottom: 0.25rem;">${disease}</li>`;
    });
    html += `</ul></div>`;
    
    // Body parts section
    html += `<div>`;
    html += `<h4 style="color: #1E40AF; margin-bottom: 0.5rem;">Related Body Parts</h4>`;
    html += `<ul style="columns: 2; column-gap: 2rem; list-style-type: disc; padding-left: 1.5rem;">`;
    data.bodyParts.forEach(part => {
      html += `<li style="margin-bottom: 0.25rem;">${part}</li>`;
    });
    html += `</ul></div>`;
    
    resultsContainer.innerHTML = html;
  } else {
    resultsContainer.innerHTML = `<p>No data available for "${letter}".</p>`;
  }
  
  // Scroll to the results
  resultsContainer.scrollIntoView({ behavior: 'smooth' });
}

// Initialize the letter buttons
function initLetterButtons() {
  const letterButtons = document.querySelectorAll('.letters a');
  
  letterButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      e.preventDefault();
      const letter = this.textContent.trim();
      displayMedicalInfo(letter);
    });
  });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initLetterButtons);